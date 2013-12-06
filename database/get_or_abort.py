# -*- coding: utf-8 -*-
"""
    database.get_or_abort
    ~~~~~~~~~~~~~~~~~~~~~

    Getting an object from a SQLAlchemy model or abort
    http://flask.pocoo.org/snippets/39/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def get_or_abort(model, object_id, code=404):
    """
    get an object with his given id or an abort error (404 is the default)
    """
    result = model.query.get(object_id)
    return result or abort(code)


def theme_detail(theme_id):
    # shows a theme
    theme = get_or_abort(Theme, theme_id)
    return render_template('theme_detail.html', theme=theme)
