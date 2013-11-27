# -*- coding: utf-8 -*-
"""
    internationalizatioin.babel_lazyproxy
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Using Babel's LazyProxy with gettext
    http://flask.pocoo.org/snippets/4/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from wtforms import Form, fields
from myapp.utils import ugettext_lazy as _
from flask import g
from babel.support import LazyProxy

from app import app


class MyForm(Form):
    name = fields.TextField(_("Name"))


def ugettext(s):
    # we assume a before_request function
    # assigns the correct user-specific
    # translations
    return g.translations.ugettext(s)


ugettext_lazy = LazyProxy(ugettext)


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
