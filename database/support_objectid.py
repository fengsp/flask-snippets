# -*- coding: utf-8 -*-
"""
    database.support_objectid
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    Support PyMongo ObjectIDs in URLs
    http://flask.pocoo.org/snippets/106/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from werkzeug.routing import BaseConverter, ValidationError
from itsdangerous import base64_encode, base64_decode
from bson.objectid import ObjectId
from bson.errors import InvalidId

from app import app


class ObjectIDConverter(BaseConverter):
    def to_python(self, value):
        try:
            return ObjectId(base64_decode(value))
        except (InvalidId, ValueError, TypeError):
            raise ValidationError()
    def to_url(self, value):
        return base64_encode(value.binary)


app.url_map.converters['objectid'] = ObjectIDConverter


@app.route('/users/<objectid:user_id>')
def show_user(user_id):
    return 'User ID: %r' % user_id
