# -*- coding: utf-8 -*-
"""
    apis.handle_accept_headers
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Handling Accept Headers
    http://flask.pocoo.org/snippets/45/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response
from flask import jsonify

from app import app


class Dummy(object):
    
    def to_json(self):
        return {'name': 'fsp'}


def get_items_from_database():
    for i in range(10):
        yield Dummy()


def request_wants_json():
    best = request.accept_mimetypes \
        .best_match(['application/json', 'text/html'])
    return best == 'application/json' and \
        request.accept_mimetypes[best] > \
        request.accept_mimetypes['text/html']


@app.route('/')
def show_items():
    items = get_items_from_database()
    if request_wants_json():
        return jsonify(items=[x.to_json() for x in items])
    return 'index'


if __name__ == "__main__":
    app.run()
