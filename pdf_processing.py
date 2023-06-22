from flask import render_template
from flask import request as rq
import pdfkit
from rq import get_current_job
import mafia_pb2

def process_tasks(task):
    path = f"player_stats_{task.username}.pdf"

    rendered_html = render_template('pdf_template.html', user=task.response)


    pdfkit.from_string(rendered_html, path,
                       configuration=pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf'))

    return f'http://127.0.0.1:5000/open_pdf/{path}'