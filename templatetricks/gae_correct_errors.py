# -*- coding: utf-8 -*-
"""
    templatetricks.gae_correct_errors
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Show correct Tracebacks for some Errors triggered inside a Template on GAE
    http://flask.pocoo.org/snippets/74/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

def format_exception(tb):
    return tb.render_as_text()
# undocumented feature
app.jinja_env.exception_formatter = format_exception


from flask import make_response
def format_exception(tb):
    res = make_response(tb.render_as_text())
    res.content_type = 'text/plain'
    return res
app.jinja_env.exception_formatter = format_exception
