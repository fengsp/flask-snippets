# -*- coding: utf-8 -*-
"""
    forms.render_wtform_without_syntaxerr
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Render WTForm fields with html attributes that cause TemplateSyntaxErrors
    http://flask.pocoo.org/snippets/107/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app import app


"""
Suppose you had a WTForm TextField that you wanted to use a javascript library like bootstrap-typeahead.js on. You might want the field to render as:

<input type="text" data-provide='typeahead', data-items='3', data-source='["x","y","z"]'>

After creating a WTForm in the view and passing it to your template, your first attempt would be to pass the additional keyword arguments:

{{ form.myfield(name='test', data-provide='typeahead', data-data-items='3', data-source='["x","y","z"]') }}

But this will lead to a TemplateSyntaxError because a dash is the subtraction operator in Python, and we can't escape the character in a keyword argument's key.

Instead, pass the HTML attributes that contain invalid syntax as an ad-hoc dictionary:

{{ form.myfield(name='test', **{'data-provide':'typeahead','data-items':'3','data-source': '["x","y","z"]'}) }}
"""
