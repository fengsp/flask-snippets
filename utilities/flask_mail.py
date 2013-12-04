# -*- coding: utf-8 -*-
"""
    utilities.flask_mail
    ~~~~~~~~~~~~~~~~~~~~

    Flask-Mail with google apps
    http://flask.pocoo.org/snippets/85/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask
from flaskext.mail import Mail, Message

app =Flask(__name__)
mail=Mail(app)

app.config.update(
    DEBUG=True,
    #EMAIL SETTINGS
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT=465,
    MAIL_USE_SSL=True,
    MAIL_USERNAME = 'you@google.com',
    MAIL_PASSWORD = 'GooglePasswordHere'
    )

mail=Mail(app)

@app.route("/")
def index():
    msg = Message(
              'Hello',
           sender='you@dgoogle.com',
           recipients=
               ['recipient@recipient_domain.com'])
    msg.body = "This is the email body"
    mail.send(msg)
    return "Sent"

if __name__ == "__main__":
    app.run()
