# -*- coding: utf-8 -*-
"""
    security.salted
    ~~~~~~~~~~~~~~~

    Salted Passwords
    http://flask.pocoo.org/snippets/54/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from werkzeug.security import generate_password_hash, check_password_hash

from app import app


class User(object):
    
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pw_hash, password)


@app.route('/')
def index():
    me = User('John Doe', 'default')
    print me.pw_hash
    print me.check_password('default')
    print me.check_password('defaultx')
    return 'index'


if __name__ == "__main__":
    app.run()
