# -*- coding: utf-8 -*-
"""
    urls.support_semicolon
    ~~~~~~~~~~~~~~~~~~~~~~

    Supporting “;” as Delimiter in Legacy Query Strings
    http://flask.pocoo.org/snippets/43/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from flask import request, Response

from app import app


class QueryStringRedirectMiddle(object):
    
    def __init__(self, application):
        self.application = application

    def __call__(self, environ, start_response):
        qs = environ.get('QUERY_STRING', '')
        environ['QUERY_STRING'] = qs.replace(';', '&')
        return self.application(environ, start_response)


@app.route('/')
def index():
    print request.args
    return 'index'


if __name__ == "__main__":
    app.wsgi_app = QueryStringRedirectMiddle(app.wsgi_app)
    app.run()
