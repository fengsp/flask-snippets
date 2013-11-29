# -*- coding: utf-8 -*-
"""
    urls.routes
    ~~~~~~~~~~~

    Helper to list routes (like Rail's rake routes)
    http://flask.pocoo.org/snippets/117/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response, url_for

from app import app


@app.route('/')
def index():
    return 'index'


@app.route('/test/<en>/', methods=['GET', 'POST'])
def test(en):
    return en


def list_routes():
    import urllib
    output = []
    for rule in app.url_map.iter_rules():
        options = {}
        for arg in rule.arguments:
            options[arg] = "[{0}]".format(arg)

        methods = ','.join(rule.methods)
        url = url_for(rule.endpoint, **options)
        # url = rule.rule
        line = urllib.unquote("{:50s} {:20s} {}".format(
            rule.endpoint, methods, url))
        output.append(line)

    for line in sorted(output):
        print line


if __name__ == "__main__":
    ctx = app.test_request_context()
    ctx.push()
    list_routes()
