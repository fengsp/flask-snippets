# -*- coding: utf-8 -*-
"""
    utilities.upload_stringio
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Upload a StringIO object with send_file
    http://flask.pocoo.org/snippets/32/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import StringIO

from flask import send_fileg

from app import app


@app.route('/')
def index():
    strIO = StringIO.StringIO()
    strIO.write('Hello from Dan Jacob and Stephane Wirtel !')
    strIO.seek(0)
    return send_file(strIO, 
                     attachment_filename="testing.txt",
                     as_attachment=True)


if __name__ == "__main__":
    app.run()
