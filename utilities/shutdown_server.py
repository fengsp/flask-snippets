# -*- coding: utf-8 -*-
"""
    utilities.shutdown_server
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Shutdown The Simple Server
    http://flask.pocoo.org/snippets/67/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request

from app import app


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.route('/shutdown', methods=['GET', 'POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'


if __name__ == "__main__":
    app.run()
