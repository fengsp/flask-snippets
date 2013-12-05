# -*- coding: utf-8 -*-
"""
    templatetricks.generate_pdf
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Generating PDF from Flask template (using xhtml2pdf)
    http://flask.pocoo.org/snippets/68/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response, render_template, redirect, url_for
from flaskext.mail import Mail, Message
from xhtml2pdf import pisa
from StringIO import StringIO

from app import app


html_content = """
<html>
    <head>
    </head>
    <body>
    {% block body %}
        <h2>Some page title.</h2>
        <table width="100%" cellpadding="4" cellspacing="0">
            <tbody>
                <tr>
                    <td width="100%">Some text.</td>
                </tr>
            </tbody>
            <tbody>
                <tr style="border: 1px solid #000000;">
                    <td width="100%">
                        <h3 style="text-align: center;">Some subtitle</h3>
                        <div>{{ g.user.get('user_attribute') }}</div>
                    </td>
                </tr>
            </tbody>
        </table>
        <hr style="margin: 3em 0;"/>
        <img src="{{ url_for('static', filename='img.png', _external=True) }}" />
    {% endblock %}
    </body>
</html>
"""


def create_pdf(pdf_data):
    pdf = StringIO()
    pisa.CreatePDF(StringIO(pdf_data.encode('utf-8')), pdf)
    return pdf


mail_ext = Mail(app)


@app.route('/your/url')
def your_view():
    subject = "Mail with PDF"
    receiver = "receiver@mail.com"
    mail_to_be_sent = Message(subject=subject, recipients=[receiver])
    mail_to_be_sent.body = "This email contains PDF."
    pdf = create_pdf(render_template('your/template.html'))
    mail_to_be_sent.attach("file.pdf", "application/pdf", pdf.getvalue())
    mail_ext.send(mail_to_be_sent)
    return redirect(url_for('other_view'))
