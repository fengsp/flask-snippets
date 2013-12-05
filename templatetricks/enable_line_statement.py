# -*- coding: utf-8 -*-
"""
    templatetricks.enable_line_statement
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Enable jinja2 line statements
    http://flask.pocoo.org/snippets/101/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


app.jinja_env.line_statement_prefix = '%'


@app.route('/')
def index():
    return 'index'


"""
<ul>
  % for item in items
    <li>{{ item }}</li>
  % endfor
</ul>
"""


if __name__ == "__main__":
    app.run()
