# -*- coding: utf-8 -*-
"""
    utilities.override_httpmethod
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Overriding HTTP Methods for old browsers
    http://flask.pocoo.org/snippets/38/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from werkzeug import url_decode

class MethodRewriteMiddleware(object):

    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        if 'METHOD_OVERRIDE' in environ.get('QUERY_STRING', ''):
            args = url_decode(environ['QUERY_STRING'])
            method = args.get('__METHOD_OVERRIDE__')
            if method:
                method = method.encode('ascii', 'replace')
                environ['REQUEST_METHOD'] = method
        return self.app(environ, start_response)


"""
<form action="?__METHOD_OVERRIDE__=PUT">
  ...
</form>
"""
