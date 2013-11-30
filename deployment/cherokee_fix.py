# -*- coding: utf-8 -*-
"""
    deployment.cherokee_fix
    ~~~~~~~~~~~~~~~~~~~~~~~

    Cherokee fix for URL prefix
    http://flask.pocoo.org/snippets/84/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


class CherrokeeFix(object):
    
    def __init__(self, app, script_name):
        self.app = app
        self.script_name = script_name

    def __call__(self, environ, start_response):
        path = environ.get('SCRIPT_NAME', '') + environ.get('PATH_INFO', '')
        environ['SCRIPT_NAME'] = self.script_name
        environ['PATH_INFO'] = path[len(self.script_name):]
        assert path[:len(self.script_name)] == self.script_name
        return self.app(environ, start_response)


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.wsgi_app = CherrokeeFix(app.wsgi_app, '/test')
    app.run()
