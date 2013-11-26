# -*- coding: utf-8 -*-
"""
    decorators.sslview
    ~~~~~~~~~~~~~~~~~~

    SSL for particular views
    http://flask.pocoo.org/snippets/93/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from flask import request, current_app, redirect

from app import app


def ssl_required(fn):
    @wraps(fn)
    def decorated_view(*args, **kwargs):
        if current_app.config.get("SSL"):
            if request.is_secure:
                return fn(*args, **kwargs)
            else:
                return redirect(request.url.replace("http://", "https://"))

        return fn(*args, **kwargs)
    
    return decorated_view


@app.route('/')
@ssl_required
def index():
    return "ssl_required"


if __name__ == "__main__":
    app.config["SSL"] = True
    app.run()
