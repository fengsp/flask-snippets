# -*- coding: utf-8 -*-
"""
    urls.permalink
    ~~~~~~~~~~~~~~

    Permalink function decorator
    http://flask.pocoo.org/snippets/6/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import url_for
from werkzeug.routing import BuildError

from app import app


def permalink(function):
    def inner(*args, **kwargs):
        endpoint, values = function(*args, **kwargs)
        try:
            return url_for(endpoint, **values)
        except BuildError:
            return
    return inner


@permalink
def absolute_url():
    return 'profiles', {'username': 'fsp'}


@app.route('/profiles/<username>/')
def profiles(username):
    return username


if __name__ == "__main__":
    ctx = app.test_request_context()
    ctx.push()
    print absolute_url()
