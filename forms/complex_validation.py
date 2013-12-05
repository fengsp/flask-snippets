# -*- coding: utf-8 -*-
"""
    forms.complex_validation
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Complex Validation with Flask-WTF
    http://flask.pocoo.org/snippets/64/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template, url_for, redirect
from flask.wtf import Form, TextField, PasswordField, validators

from app import app
from models import User


class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(u'Successfully logged in as %s' % form.user.username)
        session['user_id'] = form.user.id
        return redirect(url_for('index'))
    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()
