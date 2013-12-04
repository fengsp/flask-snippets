# -*- coding: utf-8 -*-
"""
    utilities.nice_errors
    ~~~~~~~~~~~~~~~~~~~~~

    Nicer Errors with Descriptions from Werkzeug
    http://flask.pocoo.org/snippets/15/
"""

from flask import Markup, render_template
from werkzeug.exceptions import default_exceptions

def show_errormessage(error):
    desc = error.get_description(flask.request.environ)
    return render_template('error.html',
        code=error.code,
        name=error.name,
        description=Markup(desc)
    ), error.code

for _exc in default_exceptions:
    app.error_handlers[_exc] = show_errormessage
del _exc


"""
{% extends "base.html" %}
{% block title %}Error {{ code }}: {{ name }}{% endblock %}
{% block body %}
  {{ description}}
{% endblock %}
"""
