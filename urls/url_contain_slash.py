# -*- coding: utf-8 -*-
"""
    urls.url_contain_slash
    ~~~~~~~~~~~~~~~~~~~~~~

    Handling URLs containing slash '/' character
    http://flask.pocoo.org/snippets/76/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


@app.route('/<path:test>/fsp')
def index(test):
    return test


@app.route('/product/<path:code>')
def product(code):
    return code


if __name__ == "__main__":
    app.run()
