# -*- coding: utf-8 -*-
"""
    decorators.authorization
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Simple Authorization
    http://flask.pocoo.org/snippets/98/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from app import app


def requires_roles(*roles):
    def wrapper(f):
        @wraps(f)
        def wrapped(*args, **kwargs):
            if get_current_user_role() not in roles:
                return error_response()
            return f(*args, **kwargs)
        return wrapped
    return wrapper


def get_current_user_role():
    return 'admin'


def error_response():
    return "You've got no permission to access this page.", 403


@app.route('/')
@requires_roles('admin', 'user')
def user_page():
    return "You've got permission to access this page."


if __name__ == "__main__":
    app.run()
