# -*- coding: utf-8 -*-
"""
    performance.sqlite_cache
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Cache implementation using SQLite
    http://flask.pocoo.org/snippets/87/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import os, errno, sqlite3
from time import sleep, time
from cPickle import loads, dumps
try:
    from thread import get_ident
except ImportError:
    from dummy_thread import get_ident
from werkzeug.contrib.cache import BaseCache

from app import app


class SqliteCache(BaseCache):

    _create_sql = (
            'CREATE TABLE IF NOT EXISTS bucket '
            '('
            '  key TEXT PRIMARY KEY,'
            '  val BLOB,'
            '  exp FLOAT'
            ')'
            )
    _get_sql = 'SELECT val, exp FROM bucket WHERE key = ?'
    _del_sql = 'DELETE FROM bucket WHERE key = ?'
    _set_sql = 'REPLACE INTO bucket (key, val, exp) VALUES (?, ?, ?)'
    _add_sql = 'INSERT INTO bucket (key, val, exp) VALUES (?, ?, ?)'

    def __init__(self, path, default_timeout=300):
        self.path = os.path.abspath(path)
        try:
            os.mkdir(self.path)
        except OSError, e:
            if e.errno != errno.EEXIST or not os.path.isdir(self.path):
                raise
        self.default_timeout = default_timeout
        self.connection_cache = {}

    def _get_conn(self, key):
        key = dumps(key, 0)
        t_id = get_ident()
        if t_id not in self.connection_cache:
            self.connection_cache[t_id] = {}
        if key not in self.connection_cache[t_id]:
            bucket_name = str(hash(key))
            bucket_path = os.path.join(self.path, bucket_name)
            conn = sqlite3.Connection(bucket_path, timeout=60)
            with conn:
                conn.execute(self._create_sql)
            self.connection_cache[t_id][key] = conn
        return self.connection_cache[t_id][key]

    def get(self, key):
        rv = None
        with self._get_conn(key) as conn:
            for row in conn.execute(self._get_sql, (key,)):
                expire = row[1]
                if expire > time():
                    rv = loads(str(row[0]))
                break
        return rv

    def delete(self, key):
        with self._get_conn(key) as conn:
            conn.execute(self._del_sql, (key,))

    def set(self, key, value, timeout=None):
        if not timeout:
            timeout = self.default_timeout
        value = buffer(dumps(value, 2))
        expire = time() + timeout
        with self._get_conn(key) as conn:
            conn.execute(self._set_sql, (key, value, expire))

    def add(self, key, value, timeout=None):
        if not timeout:
            timeout = self.default_timeout
        expire = time() + timeout
        value = buffer(dumps(value, 2))
        with self._get_conn(key) as conn:
            try:
                conn.execute(self._add_sql, (key, value, expire))
            except sqlite3.IntegrityError:
                pass

    def clear(self):
        for bucket in os.listdir(self.path):
            os.unlink(os.path.join(self.path, bucket))


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
