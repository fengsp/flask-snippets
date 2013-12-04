# -*- coding: utf-8 -*-
"""
    utilities.import_css_string
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Include / Import css file as string
    http://flask.pocoo.org/snippets/77/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template_string

from app import app


def get_resource_as_string(name, charset='utf-8'):
    with app.open_resource(name) as f:
        return f.read().decode(charset)

app.jinja_env.globals['get_resource_as_string'] = get_resource_as_string


"""
<style type=text/css>{{ get_resource_as_string('static/styles.css') }}</style>
"""
