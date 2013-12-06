# -*- coding: utf-8 -*-
"""
    database.sqlalchemy_test_issues
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Testing Issues with SQLAlchemy
    http://flask.pocoo.org/snippets/36/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


"""
You would like to perform some tests to ensure that you can insert and query for objects.

Insertions work, but when you try to perform a query in your tests you get a problem like this:

Failed example:
    len(MyObject.query.all())
Exception raised:
    Traceback (most recent call last):
      File ".../lib/python2.6/doctest.py", line 1248, in __run
        compileflags, 1) in test.globs
      File "<doctest myapp.MyObject[4]>", line 1, in <module>
        len(MyObject.query.all())
    AttributeError: 'NoneType' object has no attribute 'all'
What you need to do is ensure that you have initialized a request context for your tests. This can be done by:

app.test_request_context().push()
Now when you run your tests and query them they should work.
"""


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
