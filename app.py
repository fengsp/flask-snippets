# -*- coding: utf-8 -*-
"""
    flask.app
    ~~~~~~~~~

    App for flask-snippets

    :copyright: (c) 2013 by fsp.
    :license: BSD.
"""

from flask import Flask


app = Flask(__name__)
app.debug = True
app.secret_key = 'flask-snippets-fsp'


if __name__ == "__main__":
    app.run()
