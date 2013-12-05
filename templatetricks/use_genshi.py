# -*- coding: utf-8 -*-
"""
    templatetricks.use_genshi
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Using Genshi with Flask
    http://flask.pocoo.org/snippets/17/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import Flask
from flaskext.genshi import Genshi, render_response

app = Flask(__name__)
genshi = Genshi(app)

@app.route('/')
def index():
    render_response('index.html')
