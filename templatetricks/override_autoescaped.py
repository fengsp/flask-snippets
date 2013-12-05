# -*- coding: utf-8 -*-
"""
    templatetricks.override_autoescaped
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Override which templates are autoescaped
    http://flask.pocoo.org/snippets/41/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask

class JHtmlEscapingFlask(Flask):

    def select_jinja_autoescape(self, filename):
        if filename.endswith('.jhtml'):
            return True
        return Flask.select_jinja_autoescape(self, filename)

app = JHtmlEscapingFlask(__name__)
