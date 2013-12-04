# -*- coding: utf-8 -*-
"""
    utilities.reloading
    ~~~~~~~~~~~~~~~~~~~

    Reloading with other WSGI servers
    http://flask.pocoo.org/snippets/34/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import gevent.wsgi
import werkzeug.serving

from app import app


@werkzeug.serving.run_with_reloader
def runServer():
    ws = gevent.wsgi.WSGIServer(('', 5000), app)
    ws.serve_forever()


if __name__ == "__main__":
    runServer()
