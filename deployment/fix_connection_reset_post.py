# -*- coding: utf-8 -*-
"""
    deployment.fix_post_reset
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Fix for Connection Reset on POST
    http://flask.pocoo.org/snippets/47/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response
from werkzeug.wsgi import LimitedStream

from app import app


class StreamConsumingMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        stream = LimitedStream(environ['wsgi.input'],
                               int(environ['CONTENT_LENGTH'] or 0))
        environ['wsgi.input'] = stream
        app_iter = self.app(environ, start_response)
        try:
            stream.exhaust()
            for event in app_iter:
                yield event
        finally:
            if hasattr(app_iter, 'close'):
                app_iter.close()


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.wsgi_app = StreamConsumingMiddleware(app.wsgi_app)
    app.run()
