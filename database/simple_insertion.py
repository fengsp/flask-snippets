# -*- coding: utf-8 -*-
"""
    database.simple_insertion
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Simple insertion and row id
    http://flask.pocoo.org/snippets/37/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


def insert(table, fields=(), values=()):
    # g.db is the database connection
    cur = g.db.cursor()
    query = 'INSERT INTO %s (%s) VALUES (%s)' % (
        table,
        ', '.join(fields),
        ', '.join(['?'] * len(values))
    )
    cur.execute(query, values)
    g.db.commit()
    id = cur.lastrowid
    cur.close()
    return id
