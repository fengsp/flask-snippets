# -*- coding: utf-8 -*-
"""
    decorators.headers
    ~~~~~~~~~~~~~~~~~~

    Generic HTTP headers decorator
    http://flask.pocoo.org/snippets/100/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from flask import make_response

from app import app


def add_response_headers(headers={}):
    """This decorator adds the headers passed in to the response"""
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            resp = make_response(f(*args, **kwargs))
            h = resp.headers
            for header, value in headers.items():
                h[header] = value
            return resp
        return decorated_function
    return decorator


def noindex(f):
    """This decorator passes X-Robots-Tag: noindex"""
    return add_response_headers({'X-Robots-Tag': 'noindex'})(f)


@app.route('/')
@noindex
def no_indexed():
    """
    This page will be served with X-Robots-Tag: noindex
    in the response headers
    """
    return "Check my headers!"


if __name__ == "__main__":
    app.run()
    # check the headers with: curl -I http://0.0.0.0:5000/
