# -*- coding: utf-8 -*-
"""
    security.csrf
    ~~~~~~~~~~~~~

    CSRF Protection
    http://flask.pocoo.org/snippets/3/
"""

import os
import sys
from uuid import uuid4
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, session, abort
from flask import render_template_string

from app import app


@app.before_request
def csrf_protect():
    if request.method == "POST":
        token = session.pop('_csrf_token', None)
        if not token or token != request.form.get('_csrf_token'):
            abort(403)


def generate_csrf_token():
    if '_csrf_token' not in session:
        session['_csrf_token'] = str(uuid4())
    return session['_csrf_token']

app.jinja_env.globals['csrf_token'] = generate_csrf_token


@app.route('/', methods=["GET", "POST"])
def index():
    return render_template_string('<form method=post action=""><input name=_csrf_token type=hidden value="{{ csrf_token() }}"><input type="submit" value="submit"/></form>')


if __name__ == "__main__":
    app.run()
