# -*- coding: utf-8 -*-
"""
    flask-snippets.template
    ~~~~~~~~~~~~~~~~~~~~~~~

    Template Python file for flask-snippets.
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
