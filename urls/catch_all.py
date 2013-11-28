# -*- coding: utf-8 -*-
"""
    urls.catch_all
    ~~~~~~~~~~~~~~

    Catch-All URL
    http://flask.pocoo.org/snippets/57/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app import app


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return 'You want path: %s' % path


if __name__ == "__main__":
    app.run()
    """
    % curl 127.0.0.1:5000          # Matches the first rule
    % curl 127.0.0.1:5000/foo/bar  # Matches the second rule
    """
