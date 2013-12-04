# -*- coding: utf-8 -*-
"""
    utilities.local_proxy
    ~~~~~~~~~~~~~~~~~~~~~

    Creating your own local proxies
    http://flask.pocoo.org/snippets/13/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from werkzeug.local import LocalProxy

from app import app


whatever = LocalProxy(lambda: g.whatever)
method = LocalProxy(lambda: request.method)
