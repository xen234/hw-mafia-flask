from flask import render_template
from flask import request as rq
import pdfkit
from rq import get_current_job
import mafia_pb2

def process_tasks(task):
    path = f"static/player_stats_{task['username']}.pdf"

    template = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="UTF-8">
        <title>User Information</title>
    </head>
    <body>
        <h1>User Information</h1>
        <table>
            <tr>
                <th>Name</th>
                <th>Room ID</th>
                <th>Gender</th>
                <th>Email</th>
                <th>Ingame Time</th>
                <th>Lost Games</th>
                <th>Won Games</th>
            </tr>
            <tr>
                <td>{ task['username'] }</td>
                <td>{ task['room_name'] }</td>
                <td>{ task['gender'] }</td>
                <td>{ task['email'] }</td>
                <td>{ task['overall_time'] }</td>
                <td>{ task['lost'] }</td>
                <td>{ task['won'] }</td>
            </tr>
        </table>
    </body>
    </html>
    '''


    pdfkit.from_string(template, path,
                       configuration=pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf'))

    return f'http://127.0.0.1:5000/get_pdf/{path}'