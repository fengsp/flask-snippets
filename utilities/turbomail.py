# -*- coding: utf-8 -*-
"""
    utilities.turbomail
    ~~~~~~~~~~~~~~~~~~~

    Using TurboMail with Flask
    http://flask.pocoo.org/snippets/16/
"""

import atexit

from turbomail.control import interface
from turbomail.message import Message

from flask import Flask

# pass in dict of config options

interface.start({'mail.on' : True})

# ensures interface cleanly shutdown when process exits

atexit.register(interface.stop, force=True)

app = Flask(__name__)

@app.route("/")
def index():
    # send an email
    msg = Message("from@example.com",
                  "to@example.com",
                  "a subject")
    msg.plain = "body of message"
    msg.send()
