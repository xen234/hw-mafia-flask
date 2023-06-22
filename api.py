import os
from rq import Queue
from rq.job import Job
import redis
from flask import Flask, render_template, flash, redirect, send_from_directory, jsonify, send_file
from flask import request as rq
import grpc
from werkzeug.utils import secure_filename
from pdf_processing import *

import mafia_pb2
import mafia_pb2_grpc
import uuid

from threading import Thread
import pdfkit
from worker import conn


app = Flask(__name__)
task_queue = Queue(connection=conn)


recommendations_host = os.getenv("RECOMMENDATIONS_HOST", "server")
recommendations_channel = grpc.insecure_channel(
    f"{recommendations_host}:50051"
)
stub = mafia_pb2_grpc.MafiaStub(recommendations_channel)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
app.config['UPLOAD_FOLDER'] = 'static'


@app.route("/")
def render_homepage():
    return render_template("basic_template.html")


@app.route('/user/<room_id>/<user_id>', methods=['GET'])
def get_user(room_id, user_id):

    request = mafia_pb2.UserInfoRequest(room_name = room_id, username = user_id)
    response = stub.UserInfo(request)

    return render_template(
        "userpage.html",
        data=response,
    )


@app.route('/user/<room_id>', methods=['GET'])
def get_users_by_room(room_id):
    request = mafia_pb2.RoomUsersRequest(room_name = room_id)
    response = stub.RoomUsers(request)
    rendered_templates = []

    for user in response.users[:]:
        another_request = mafia_pb2.UserInfoRequest(room_name = room_id, username = user)
        another_response = stub.UserInfo(another_request)

        rendered_template = render_template("userpage.html", data=another_response)
        rendered_templates.append(rendered_template)

    return '\n'.join(rendered_templates)


@app.route('/change/<room_name>/<user_id>', methods=['GET'])
def change_profile(room_name, user_id):
    gender = rq.args.get('gender')
    email = rq.args.get('email')

    request = mafia_pb2.ChangeUserInfoRequest(room_name = room_name, 
                                              username = user_id, gender=gender, email=email)
    response = stub.ChangeUserInfo(request)

    return 'Info changed'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/set_avatar/<room_name>/<username>', methods=['POST', 'GET'])
def upload_file(room_name, username):
    if rq.method == 'POST':
        # check if the post request has the file part
        if 'file' not in rq.files:
            flash('No file part')
            return redirect(rq.url)
        file = rq.files['file']
        # if user does not select file, browser also
        # submit a empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(rq.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            request = stub.SetAvatar(mafia_pb2.SetAvatarRequest(room_name=room_name, username=username, filename=filename))
        return 'File uploaded successfully'
    return '''
    <!doctype html>
    <h2>Upload Avatar</h2>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    '''

@app.route('/<room_name>/<user>/avatar')
def display_file(room_name, user):
    request = mafia_pb2.UserInfoRequest(room_name = room_name, username = user)
    response = stub.UserInfo(request)
    return send_from_directory(app.config['UPLOAD_FOLDER'], response.filename)


# PDF GENERATION AND QUEUE

@app.route('/<room_name>/<user>/generate-pdf', methods=['POST'])
def generate_pdf_endpoint(room_name, user):

    request = mafia_pb2.UserInfoRequest(room_name = room_name, username = user)
    response = stub.UserInfo(request)

    task = {'room_name': room_name, 'username': user, 'gender' : response.gender, 'email' : response.email, 'won' : response.won, 
            'lost' : response.lost, 'overall_time' : response.overall_time}
    job = task_queue.enqueue(process_tasks, task)

    return jsonify({'job_id': job.id}), 202


@app.route('/jobs/<job_id>', methods=['GET'])
def get_job_status(job_id):
    job = Job.fetch(job_id, connection=conn)

    if job is None:
        return jsonify({'error': 'Invalid job ID'}), 404

    if job.is_finished:
        result = job.result
        return jsonify(result), 200
    elif job.is_failed:
        return jsonify({'error': 'Failed to generate PDF'}), 500
    else:
        return jsonify({'status': 'in progress'}), 202
    

@app.route('/get_pdf/static/<pdf_file>', methods=['GET'])
def get_pdf_document(pdf_file):
    pdf_directory = 'static'

    pdf_path = os.path.join(app.root_path, pdf_directory, pdf_file)

    if not os.path.isfile(pdf_path):
        return 'PDF file not found'

    return send_from_directory(pdf_directory, pdf_file, as_attachment=True)
    


if __name__ == '__main__':
    app.run(host="0.0.0.0", port="3001")