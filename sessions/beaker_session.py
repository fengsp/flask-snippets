# -*- coding: utf-8 -*-
"""
    sessions.beaker_session
    ~~~~~~~~~~~~~~~~~~~~~~~

    Using Beaker session with Flask
    http://flask.pocoo.org/snippets/61/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request
from beaker.middleware import SessionMiddleware

from app import app


session_opts = {
    'session.type': 'ext:memcached',
    'session.url': '127.0.0.1:11211',
    'session.data_dir': './cache',
}


@app.route('/')
def index():
    session = request.environ['beaker.session']
    if not session.has_key('value'):
        session['value'] = 'Save in session' 
        session.save()   
        return "Session value set."
    else:
        return session['value']
    
if __name__ == '__main__':
    app.wsgi_app = SessionMiddleware(app.wsgi_app, session_opts)
    app.run(debug=True)
