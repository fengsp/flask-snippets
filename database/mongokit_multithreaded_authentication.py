# -*- coding: utf-8 -*-
"""
    database.mongokit_multithreaded_authentication
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    MongoKit multithreaded authentication
    http://flask.pocoo.org/snippets/66/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))


class ThreadLocalConnectionProxy(object):
    """
    A proxy object for a MongoKit connection object. As pymongo authentication
    is thread local, we need a seperate connection for each thread, which this
    proxy provides in a transparent manner.
    """
    def __init__(self, logger):
        self.logger = logger
    
    def connect(self):
        """
        Sets the thread local `mongodb_connection` attribute to a new connection
        aquired with :func:`get_connection`.
        """
        self.thread_local.mongodb_connection = get_connection(self.logger)
    
    @property
    def connected(self):
        """
        Returns true if there is a connection object in the thread local
        storage.
        """
        return hasattr(self.thread_local, "mongodb_connection")
    
    @property
    def thread_local(self):
        """
        Thread local storage if possible, else object global.
        """
        return flask._request_ctx_stack.top or self
    
    def __getattr__(self, name):
        if name == "logger":
            return super(ThreadLocalConnectionProxy, self).logger
        if not self.connected:
            self.connect()
        return getattr(self.thread_local.mongodb_connection, name)
