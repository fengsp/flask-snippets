# -*- coding: utf-8 -*-
"""
    utilities.trigger_debugger
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Triggering the debugger on purpose
    http://flask.pocoo.org/snippets/21/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template_string

from app import app


@app.route('/')
def index():
   do_something_wrong()
   raise
   return 'Ohnoes'


"""
assert app.debug == False
"""
