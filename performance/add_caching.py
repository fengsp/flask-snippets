# -*- coding: utf-8 -*-
"""
    performance.caching
    ~~~~~~~~~~~~~~~~~~~

    Adding caching to Flask apps
    http://flask.pocoo.org/snippets/9/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from werkzeug.contrib.cache import SimpleCache
from flask import request

from app import app


CACHE_TIMEOUT = 300


cache = SimpleCache()


class cached(object):
    
    def __init__(self, timeout=None):
        self.timeout = timeout or CACHE_TIMEOUT

    def __call__(self, f):
        def decorator(*args, **kwargs):
            response = cache.get(request.path)
            if response is None:
                response = f(*args, **kwargs)
                cache.set(request.path, response, self.timeout)
            return response
        return decorator


@app.route('/')
# @cached()
def index():
    return 'index'


@app.before_request
def return_cached():
    # if GET and POST not empty
    if not request.values:
        response = cache.get(request.path)
        if response:
            return response


@app.after_request
def cache_response(response):
    if not request.values:
        cache.set(request.path, response, CACHE_TIMEOUT)
    return response


if __name__ == "__main__":
    app.run()
