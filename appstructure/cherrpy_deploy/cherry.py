# -*- coding: utf-8 -*-
from cherrypy import wsgiserver

from hello import app


d = wsgiserver.WSGIPathInfoDispatcher({'/': app})
server = wsgiserver.CherryPyWSGIServer(('0.0.0.0', 8080), d)


if __name__ == "__main__":
    try:
        server.start()
    except KeyboardInterrupt:
        server.stop()
