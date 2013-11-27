# -*- coding: utf-8 -*-
"""
    security.rback
    ~~~~~~~~~~~~~~

    Securely Redirect Back
    http://flask.pocoo.org/snippets/62/
"""

import os
import sys
from urlparse import urlparse, urljoin
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, url_for, redirect
from flask import render_template_string

from app import app


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


def redirect_back(endpoint, **values):
    target = request.form['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)


@app.route('/')
def index():
    return 'index'


@app.route('/fsp')
def fsp():
    return 'fsp'


@app.route('/login', methods=['GET', 'POST'])
def login():
    next = get_redirect_target()
    html_content = """
<form action="" method=post>
  <dl>
    <dt>Username:
    <dd><input type=text name=username>
    <dt>Password:
    <dd><input type=password name=password>
  </dl>
  <p>
    <input type=submit value=Login>
    <input type=hidden value="{{ next or '' }}" name=next>
</form>
"""
    if request.method == 'POST':
        # Login code here
        return redirect_back('index')
    return render_template_string(html_content, next=next)


if __name__ == "__main__":
    app.run()
