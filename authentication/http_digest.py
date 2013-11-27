# -*- coding: utf-8 -*-
"""
    authentication.digest
    ~~~~~~~~~~~~~~~~~~~~~

    HTTP Digest Auth
    http://flask.pocoo.org/snippets/31/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from werkzeug.contrib import authdigest
import flask
from flask import request, session

from app import app


from functools import wraps
from werkzeug.contrib import authdigest
import flask

class FlaskRealmDigestDB(authdigest.RealmDigestDB):
    def requires_auth(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            request = flask.request
            if not self.isAuthenticated(request):
                return self.challenge()

            return f(*args, **kwargs)

        return decorated


authDB = FlaskRealmDigestDB('MyAuthRealm')
authDB.add_user('admin', 'test')


@app.route('/')
@authDB.requires_auth
def auth():
    session['user'] = request.authorization.username
    return "<h1>Content for authenticated user</h1>"


@app.route('/auth')
def authApi():
    if not authDB.isAuthenticated(request):
        return authDB.challenge()

    session['user'] = request.authorization.username
    return "<h1>Content for authenticated user</h1>"


if __name__ == "__main__":
    app.run()
