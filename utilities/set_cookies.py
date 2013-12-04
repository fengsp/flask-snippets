# -*- coding: utf-8 -*-
"""
    utilities.set_cookies
    ~~~~~~~~~~~~~~~~~~~~~

    Flask Set Cookies by Response
    http://flask.pocoo.org/snippets/30/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import redirect, current_app

from app import app


@app.route('/set_cookie')
def cookie_insertion():
    redirect_to_index = redirect('/index')
    response = current_app.make_response(redirect_to_index)
    response.set_cookie('cookie_name',value='values')
    return response
