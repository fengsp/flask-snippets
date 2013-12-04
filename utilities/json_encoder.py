# -*- coding: utf-8 -*-
"""
    utilities.json_encoder
    ~~~~~~~~~~~~~~~~~~~~~~

    Custom Flask JSONEncoder
    http://flask.pocoo.org/snippets/119/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from datetime import datetime
import calendar

from flask import jsonify
from flask.json import JSONEncoder

from app import app


class CustomJSONEncoder(JSONEncoder):
    
    def default(self, obj):
        try:
            if isinstance(obj, datetime):
                if obj.utcoffset() is not None:
                    obj = obj - obj.utcoffset()
                millis = int(
                    calendar.timegm(obj.timetuple()) * 1000 +
                    obj.microsecond / 1000
                )
                return millis
            iterable = iter(obj)
        except TypeError:
            pass
        else:
            return list(iterable)
        return JSONEncoder.default(self, obj)


app.json_encoder = CustomJSONEncoder


@app.route('/custom')
def custom_jsonencoder():
    now = datetime.now()
    return jsonify({'now': now})


if __name__ == '__main__':
    app.run()
