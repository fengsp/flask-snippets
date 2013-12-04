# -*- coding: utf-8 -*-
"""
    utilities.share_server
    ~~~~~~~~~~~~~~~~~~~~~~

    Share your Local Server with a Friend
    http://flask.pocoo.org/snippets/89/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template_string

from app import app


"""
$ sudo gem install localtunnel
$ localtunnel 5000
$ Port 5000 is now publicly accessible from http://54xy.localtunnel.com ...
"""
