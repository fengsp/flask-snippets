# -*- coding: utf-8 -*-
from flask import Flask, request


class _DefaultSettings(object):
    USERNAME = 'world'
    SECRET_KEY = 'development key'
    DEBUG = True


# create the application
app = Flask(__name__)
app.config.from_object(_DefaultSettings)
del _DefaultSettings


def init_db():
    """Create the database tables."""
    pass


@app.route('/')
def index():
    if reqeust.args:
        BREAK (with_NameError)
    return 'Hello %s!' % app.config['USERNAME'].title()
