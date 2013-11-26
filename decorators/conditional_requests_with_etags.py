# -*- coding: utf-8 -*-
"""
    decorators.etags
    ~~~~~~~~~~~~~~~~

    Conditional Requests with ETags
    http://flask.pocoo.org/snippets/95/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import functools
import hashlib

import flask
import werkzeug

from app import app


def conditional(func):
    '''Start conditional method execution for this resource'''
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        flask.g.condtnl_etags_start = True
        return func(*args, **kwargs)
    return wrapper


_old_set_etag = werkzeug.ETagResponseMixin.set_etag
@functools.wraps(werkzeug.ETagResponseMixin.set_etag)
def _new_set_etag(self, etag, weak=False):
    # only check the first time through; when called twice
    # we're modifying
    if (hasattr(flask.g, 'condtnl_etags_start') and
                                flask.g.condtnl_etags_start):
        if flask.request.method in ('PUT', 'DELETE', 'PATCH'):
            if not flask.request.if_match:
                raise PreconditionRequired
            if etag not in flask.request.if_match:
                flask.abort(412)
        elif (flask.request.method == 'GET' and
              flask.request.if_none_match and
              etag in flask.request.if_none_match):
            raise NotModified
        flask.g.condtnl_etags_start = False
    _old_set_etag(self, etag, weak)
werkzeug.ETagResponseMixin.set_etag = _new_set_etag


d = {'a': 'This is "a".\n', 'b': 'This is "b".\n'}


@app.route('/<path>', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
@conditional
def view(path):
    try:
        # SHA1 should generate well-behaved etags
        etag = hashlib.sha1(d[path]).hexdigest()
        if flask.request.method == 'GET':
            response = flask.make_response(d[path])
            response.set_etag(etag)
        else:
            response = flask.Response(status=204)
            del response.headers['content-type']
            response.set_etag(etag)
            if flask.request.method == 'DELETE':
                del d[path]
                del response.headers['etag']
            else:
                if flask.request.method == 'PUT':
                    d[path] = flask.request.data
                else: # (PATCH)
                    # Lame PATCH technique
                    d[path] += flask.request.data
                response.set_etag(hashlib.sha1(d[path]).hexdigest())
        return response
    except KeyError:
        flask.abort(404)


class NotModified(werkzeug.exceptions.HTTPException):
    code = 304
    def get_response(self, environment):
        return flask.Response(status=304)


class PreconditionRequired(werkzeug.exceptions.HTTPException):
    code = 428
    description = ('<p>This request is required to be '
                   'conditional; try using "If-Match".')
    name = 'Precondition Required'
    def get_response(self, environment):
        resp = super(PreconditionRequired,
                     self).get_response(environment)
        resp.status = str(self.code) + ' ' + self.name.upper()
        return resp


if __name__ == "__main__":
    app.run()
    # Testing with curl
    # $ curl -i localhost:5000/a

    # $ curl -iH 'If-None-Match: \
    #   "56eaadbbd9fa287e7270cf13a41083c94f52ab9b"' localhost:5000/a

    # $ curl -iX DELETE localhost:5000/a

    # $ curl -iX DELETE -H 'If-Match: "badmatch"' localhost:5000/a

    # $ curl -iX DELETE -H 'If-Match: \
    # "56eaadbbd9fa287e7270cf13a41083c94f52ab9b"' localhost:5000/a

    # $ curl -i localhost:5000/a
