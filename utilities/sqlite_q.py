# -*- coding: utf-8 -*-
"""
    utilities.sqlite_q
    ~~~~~~~~~~~~~~~~~~

    Job queue implemented using SQLite
    http://flask.pocoo.org/snippets/88/
"""

import os, sqlite3
from cPickle import loads, dumps
from time import sleep
try:
    from thread import get_ident
except ImportError:
    from dummy_thread import get_ident


class SqliteQueue(object):

    _create = (
            'CREATE TABLE IF NOT EXISTS queue ' 
            '('
            '  id INTEGER PRIMARY KEY AUTOINCREMENT,'
            '  item BLOB'
            ')'
            )
    _count = 'SELECT COUNT(*) FROM queue'
    _iterate = 'SELECT id, item FROM queue'
    _append = 'INSERT INTO queue (item) VALUES (?)'
    _write_lock = 'BEGIN IMMEDIATE'
    _popleft_get = (
            'SELECT id, item FROM queue '
            'ORDER BY id LIMIT 1'
            )
    _popleft_del = 'DELETE FROM queue WHERE id = ?'
    _peek = (
            'SELECT item FROM queue '
            'ORDER BY id LIMIT 1'
            )

    def __init__(self, path):
        self.path = os.path.abspath(path)
        self._connection_cache = {}
        with self._get_conn() as conn:
            conn.execute(self._create)

    def __len__(self):
        with self._get_conn() as conn:
            l = conn.execute(self._count).next()[0]
        return l

    def __iter__(self):
        with self._get_conn() as conn:
            for id, obj_buffer in conn.execute(self._iterate):
                yield loads(str(obj_buffer))

    def _get_conn(self):
        id = get_ident()
        if id not in self._connection_cache:
            self._connection_cache[id] = sqlite3.Connection(self.path, 
                    timeout=60)
        return self._connection_cache[id]

    def append(self, obj):
        obj_buffer = buffer(dumps(obj, 2))
        with self._get_conn() as conn:
            conn.execute(self._append, (obj_buffer,)) 

    def popleft(self, sleep_wait=True):
        keep_pooling = True
        wait = 0.1
        max_wait = 2
        tries = 0
        with self._get_conn() as conn:
            id = None
            while keep_pooling:
                conn.execute(self._write_lock)
                cursor = conn.execute(self._popleft_get)
                try:
                    id, obj_buffer = cursor.next()
                    keep_pooling = False
                except StopIteration:
                    conn.commit() # unlock the database
                    if not sleep_wait:
                        keep_pooling = False
                        continue
                    tries += 1
                    sleep(wait)
                    wait = min(max_wait, tries/10 + wait)
            if id:
                conn.execute(self._popleft_del, (id,))
                return loads(str(obj_buffer))
        return None

    def peek(self):
        with self._get_conn() as conn:
            cursor = conn.execute(self._peek)
            try:
                return loads(str(cursor.next()[0]))
            except StopIteration:
                return None
