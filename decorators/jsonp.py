# -*- coding: utf-8 -*-
"""
    decorators.jsonp
    ~~~~~~~~~~~~~~~~

    JSONP decorator
    http://flask.pocoo.org/snippets/79/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from flask import request, current_app
from flask import jsonify

from app import app


def jsonp(func):
    """Wraps JSONified output for JSONP requests."""
    @wraps(func)
    def decorated_function(*args, **kwargs):
        callback = request.args.get('callback', False)
        if callback:
            data = str(func(*args, **kwargs).data)
            content = str(callback) + '(' + data + ')'
            mimetype = 'application/javascript'
            return current_app.response_class(content, mimetype=mimetype)
        else:
            return func(*args, **kwargs)
    return decorated_function

    
@app.route('/')
@jsonp
def jsonped():
    return jsonify({"foo": "bar"})


if __name__ == "__main__":
    app.run()
