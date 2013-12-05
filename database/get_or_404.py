# -*- coding: utf-8 -*-
"""
    database.get_or_404
    ~~~~~~~~~~~~~~~~~~~

    get_object_or_404
    http://flask.pocoo.org/snippets/115/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from sqlalchemy.orm import exc
from werkzeug.exceptions import abort


def get_object_or_404(model, *criterion):
    try:
        rv = model.query.filter(*criterion).one()
    except exc.NoResultFound, exc.MultipleResultsFound:
        abort(404)
    else:
        return rv


board = get_object_or_404(Board, Board.slug == slug)
user = get_object_or_404(User, User.id == id)
