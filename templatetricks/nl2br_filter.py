# -*- coding: utf-8 -*-
"""
    templatetricks.nl2br_filter
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    nl2br filter
    http://flask.pocoo.org/snippets/28/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import re

from jinja2 import evalcontextfilter, Markup, escape

from app import app


_paragraph_re = re.compile(r'(?:\r\n|\r|\n){2,}')


@app.template_filter()
@evalcontextfilter
def nl2br(eval_ctx, value):
    result = u'\n\n'.join(u'<p>%s</p>' % p.replace('\n', '<br>\n') \
        for p in _paragraph_re.split(escape(value)))
    if eval_ctx.autoescape:
        result = Markup(result)
    return result
