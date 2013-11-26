# -*- coding: utf-8 -*-
"""
    security.https
    ~~~~~~~~~~~~~~

    How to serve HTTPS *directly* from Flask 
    http://flask.pocoo.org/snippets/111/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from OpenSSL import SSL

from app import app


context = SSL.Context(SSL.SSLv23_METHOD)
context.use_privatekey_file('yourserver.key')
context.use_certificate_file('yourserver.crt')


@app.route('/')
def index():
    return 'index'


"""
    Linux-related:
    there is a confirmed bug in pyOpenSSL that generates a runtime error:
    https://bugs.launchpad.net/pyopenssl/+bug/900792

    The workaround is to put these 2 lines in werkzeug/serving.py

    in class BaseWSGIServer(HTTPServer, object):
    ...
     def shutdown_request(self,request):
            request.shutdown()
"""


if __name__ == "__main__":
    app.run(ssl_context=context)
