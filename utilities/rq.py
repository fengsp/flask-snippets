# -*- coding: utf-8 -*-
"""
    utilities.rq
    ~~~~~~~~~~~~

    Basic Message Queue with Redis
    http://flask.pocoo.org/snippets/73/
"""

import os
import sys
from uuid import uuid4
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from pickle import loads, dumps

from redis import Redis
from flask import current_app
from flask import session, abort, jsonify

from app import app


# Connecting to Redis
redis = Redis()


# The Configuration
app.config['REDIS_QUEUE_KEY'] = 'my_queue'


class DelayedResult(object):
    def __init__(self, key):
        self.key = key
        self._rv = None

    @property
    def return_value(self):
        if self._rv is None:
            rv = redis.get(self.key)
            if rv is not None:
                self._rv = loads(rv)
        return self._rv


def queuefunc(f):
    def delay(*args, **kwargs):
        qkey = current_app.config['REDIS_QUEUE_KEY']
        key = '%s:result:%s' % (qkey, str(uuid4()))
        s = dumps((f, key, args, kwargs))
        redis.rpush(current_app.config['REDIS_QUEUE_KEY'], s)
        return DelayedResult(key)
    f.delay = delay
    return f


def queue_daemon(app, rv_ttl=500):
    while 1:
        msg = redis.blpop(app.config['REDIS_QUEUE_KEY'])
        func, key, args, kwargs = loads(msg[1])
        try:
            rv = func(*args, **kwargs)
        except Exception, e:
            rv = e
        if rv is not None:
            redis.set(key, dumps(rv))
            redis.expire(key, rv_ttl)


@queuefunc
def add(a, b):
    return a + b


@app.route('/add')
def add_numbers():
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    if a is None or b is None:
        abort(400)
    rv = add.delay(a, b)
    session['add_result_key'] = rv.key
    return 'Waiting for result...'


@app.route('/add-result')
def add_numbers_result():
    key = session.get('add_result_key')
    if key is None:
        return jsonify(ready=False)
    rv = DelayedResult(key)
    if rv.return_value is None:
        return jsonify(ready=False)
    redis.delete(key)
    del session['add_result_key']
    return jsonify(ready=True, result=rv.return_value)


if __name__ == "__main__":
    ctx = app.test_request_context()
    ctx.push()
    rv = add.delay(1, 2)
    import threading
    daemon = threading.Thread(target=queue_daemon, args=(app,))
    daemon.setDaemon(True)
    daemon.start()
    while True:
        rt = rv.return_value
        if rt is None:
            continue
        else:
            print rt
            print rv.key
            break
