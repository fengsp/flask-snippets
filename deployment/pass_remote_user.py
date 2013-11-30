# -*- coding: utf-8 -*-
"""
    deployment.pass_remote_user
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Passing REMOTE_USER from Apache as a reverse proxy to web application servers
    http://flask.pocoo.org/snippets/69/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


"""
RequestHeader set X-Proxy-REMOTE-USER %{REMOTE_USER}
"""


class RemoteUserMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        user = environ.pop('HTTP_X_PROXY_REMOTE_USER', None)
        environ['REMOTE_USER'] = user
        return self.app(environ, start_response)


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.wsgi_app = RemoteUserMiddleware(app.wsgi_app)
    app.run()
