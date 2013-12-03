# -*- coding: utf-8 -*-
from flask import Flask

import websiteconfig

app = Flask(__name__)


app.debug = websiteconfig.DEBUG
app.secret_key = websiteconfig.SECRET_KEY


@app.route("/")
def hello():
    return "Hello World!"
