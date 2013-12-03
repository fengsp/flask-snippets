# -*- coding: utf-8 -*-
"""
    appstructure.admin_blueprint
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Admin Blueprint
    http://flask.pocoo.org/snippets/59/
"""

from flask import Flask
import admin


app = Flask(__name__)
app.register_blueprint(admin.bp, url_prefix='/admin')
