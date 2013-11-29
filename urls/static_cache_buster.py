# -*- coding: utf-8 -*-
"""
    urls.static_cache_buster
    ~~~~~~~~~~~~~~~~~~~~~~~~

    static url cache buster
    http://flask.pocoo.org/snippets/40/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response, url_for

from app import app


"""
<link rel="stylesheet" href="/static/css/reset.css?q=1280549780"
   type="text/css" media="screen" charset="utf-8" />
"""


@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path, endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


@app.route('/')
def index():
    return dated_url_for('static', filename='fsp.jpg')


if __name__ == "__main__":
    app.run()
