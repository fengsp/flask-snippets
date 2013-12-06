# -*- coding: utf-8 -*-
"""
    sessions.unittest_example
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Unittest example with before and after function calls
    http://flask.pocoo.org/snippets/58/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def test_set_date_range(self):
    arg_dict = {
            'min_date': "2011-7-1",
            'max_date': "2011-7-4",
    }
    with self.app.test_request_context('/date_range/',
                method="POST", data=arg_dict):

        # call the before funcs
        rv = self.app.preprocess_request()
        if rv != None:
            response = self.app.make_response(rv)
        else:
            # do the main dispatch
            rv = self.app.dispatch_request()
            response = self.app.make_response(rv)

            # now do the after funcs
            response = self.app.process_response(response)

    assert response.mimetype == 'application/json'
    assert "OK" in response.data
