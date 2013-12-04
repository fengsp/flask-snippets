# -*- coding: utf-8 -*-
"""
    utilities.context_global_socketio
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Using Context Globals with Gevent-Socketio
    http://flask.pocoo.org/snippets/105/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from socketio import socketio_manage
@app.route('/socket.io/<path:path>')
def run_socketio(path):
    real_request = request._get_current_object()
    socketio_manage(request.environ, {'': FlaskNamespace},
            request=real_request)
    return Response()

from socketio.namespace import BaseNamespace
class FlaskNamespace(BaseNamespace):
    def __init__(self, *args, **kwargs):
        request = kwargs.get('request', None)
        self.ctx = None
        if request:
            self.ctx = current_app.request_context(request.environ)
            self.ctx.push()
            current_app.preprocess_request()
            del kwargs['request']
        super(BaseNamespace, self).__init__(*args, **kwargs)

    def disconnect(self, *args, **kwargs):
        if self.ctx:
            self.ctx.pop()
        super(BaseNamespace, self).disconnect(*args, **kwargs)
