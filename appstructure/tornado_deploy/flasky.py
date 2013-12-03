# -*- coding: utf-8 -*-
from flask import Flask


app = Flask(__name__)


@app.route("/flask")
def hello_world():
    return 'This comes from Flask ^_^'
