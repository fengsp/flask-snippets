# -*- coding: utf-8 -*-
"""
    utilities.stream_proxy
    ~~~~~~~~~~~~~~~~~~~~~~

    Stream Proxy with Requests
    http://flask.pocoo.org/snippets/118/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Response, stream_with_context
import requests

from app import app


@app.route('/<path:url>')
def home(url):
    req = requests.get(url, stream=True)
    return Response(stream_with_context(req.iter_content()), content_type = req.headers['content-type'])


if __name__ == '__main__':
    app.run()
