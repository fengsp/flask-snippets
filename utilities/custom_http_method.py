# -*- coding: utf-8 -*-
"""
    utilities.custom_http_method
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Custom HTTP methods
    http://flask.pocoo.org/snippets/1/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template_string

from app import app


@app.before_request
def before_request():
    method = request.form.get('_method', '').upper()
    if method:
        request.environ['REQUEST_METHOD'] = method
        ctx = flask._request_ctx_stack.top
        ctx.url_adapter.default_method = method
        assert request.method == method


@app.route('/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    pass

"""
<form action="{{ url_for('delete_entry', id=10) }}" method="POST">
    <input type="hidden" name="_method" value="DELETE" />
    <input type="submit" value="Delete entry 10" />
</form>
"""
