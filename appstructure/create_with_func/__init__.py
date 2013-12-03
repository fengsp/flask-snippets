# -*- coding: utf-8 -*-
"""
    appstructure.create_with_func
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Create your app with a function
    http://flask.pocoo.org/snippets/20/
"""

from flask import Flask
from sqlalchemy import create_engine

from myapp import config
from myapp.views import frontend


def create_app(database_uri, debug=False):
    app = Flask(__name__)
    app.debug = debug

    # set up your database
    app.engine = create_engine(database_uri)

    # add your modules
    app.register_module(frontend)

    # other setup tasks

    return app


if __name__ == "__main__":
    app = create_app(config.DATABASE_URI, debug=True)
    app.run()
"""
import unittest

from myapp import config
from myapp import create_app

class TestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app(config.TEST_DATABASE_URI)
        self.client = self.app.test_client()
"""
