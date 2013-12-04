# -*- coding: utf-8 -*-
"""
    utilities.after_request_per
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Per-Request After-Request Callbacks
    http://flask.pocoo.org/snippets/53/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import g

from app import app


def after_this_request(func):
    if not hasattr(g, 'call_after_request'):
        g.call_after_request = []
    g.call_after_request.append(func)
    return func


@app.after_request
def per_request_callbacks(response):
    for func in getattr(g, 'call_after_request', ()):
        response = func(response)
    return response


def invalidate_username_cache():
    @after_this_request
    def delete_username_cookie(response):
        response.delete_cookie('username')
        return response
