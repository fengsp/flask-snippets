# -*- coding: utf-8 -*-
"""
    database.simple_persistence
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Simple persistence
    http://flask.pocoo.org/snippets/25/
"""

from __future__ import with_statement
import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import shelve
from os import path
from cPickle import HIGHEST_PROTOCOL
from contextlib import closing

from app import app


SHELVE_DB = 'shelve.db'
app.config['SHELVE_DB'] = SHELVE_DB


db = shelve.open(path.join(app.root_path, app.config['SHELVE_DB']),
                 protocol=HIGHEST_PROTOCOL, writeback=True)


@app.route('/<message>')
def write_and_list(message):
    db.setdefault('messages', [])
    db['messages'].append(message)
    return app.response_class('\n'.join(db['messages']), mimetype='text/plain')


if __name__ == '__main__':
    with closing(db):
        app.run()
