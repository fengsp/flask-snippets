# -*- coding: utf-8 -*-
"""
    utilities.wtform_flash_error
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Flashing errors from WTForms forms
    http://flask.pocoo.org/snippets/12/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template_string

from app import app


def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,
                error
            ))
