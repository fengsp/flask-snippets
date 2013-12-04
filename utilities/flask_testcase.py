# -*- coding: utf-8 -*-
"""
    utilities.flask_testcase
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Flask TestCase
    http://flask.pocoo.org/snippets/26/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import unittest

from flask import render_template_string

from app import app


class TestCase(unittest.TestCase):

    def create_app(self):
        """
        Create your Flask app here, with any
        configuration you need
        """
        raise NotImplementedError

    def __call__(self, result=None):
       """
       Does the required setup, doing it here
       means you don't have to call super.setUp
       in subclasses.
       """
       self._pre_setup()
       super(TestCase, self).__call__(result)
       self._post_tearDown()

    def _pre_setup(self):
       self.app = self.create_app()
       self.client = self.app.test_client()
       
       # now you can use flask thread locals

       self._ctx = self.app.test_request_context()
       self._ctx.push()

    def _post_tearDown(self):
       self._ctx.pop()

    def assert404(self, response):
        """
        Checks if a HTTP 404 returned
        e.g. 
        resp = self.client.get("/")
        self.assert404(resp)
        """
        self.assertTrue(response.status_code == 404)
