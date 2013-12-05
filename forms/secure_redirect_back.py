# -*- coding: utf-8 -*-
"""
    forms.secure_redirect_back
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Secure Back Redirects with WTForms
    http://flask.pocoo.org/snippets/63/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from urlparse import urlparse, urljoin

from flask import request, url_for, redirect
from flaskext.wtf import Form, TextField, HiddenField

from app import app


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc


def get_redirect_target():
    for target in request.args.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target


class RedirectForm(Form):
    next = HiddenField()

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        if not self.next.data:
            self.next.data = get_redirect_target() or ''

    def redirect(self, endpoint='index', **values):
        if is_safe_url(self.next.data):
            return redirect(self.next.data)
        target = get_redirect_target()
        return redirect(target or url_for(endpoint, **values))


class LoginForm(RedirectForm):
    username = TextField('Username')
    password = TextField('Password')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # do something with the form data here
        return form.redirect('index')
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
