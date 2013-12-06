# -*- coding: utf-8 -*-
"""
    sessions.old_new_session
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Support for Old and New Sessions
    http://flask.pocoo.org/snippets/52/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
try:
    from flask.sessions import SessionMixin, SessionInterface
except ImportError:
    class SessionInterface(object):
        pass

    class SessionMixin(object):
        def _get_permanent(self):
            return self.get('_permanent', False)
        def _set_permanent(self, value):
            self['_permanent'] = bool(value)
        permanent = property(_get_permanent, _set_permanent)
        del _get_permanent, _set_permanent

        # you can use a werkzeug.datastructure.CallbackDict
        # to automatically update modified if you want, but
        # it's not a requirement.
        new = False
        modified = True


class MySession(dict, SessionMixin):
     pass


class MySessionInterface(object):

    def open_session(self, app, request):
        # load the session and return it.
        return MySession()

    def save_session(self, app, session, response):
        # save the session
        ...


def init_my_extension(app):
    if not hasattr(app, 'session_interface'):
        app.open_session = lambda r: \
            app.session_interface.open_session(app, r)
        app.save_session = lambda s, r: \
            app.session_interface.save_session(app, s, r)
    app.session_interface = MySessionInterface()
