# -*- coding: utf-8 -*-
"""
    deployment.webfaction
    ~~~~~~~~~~~~~~~~~~~~~

    Deploying a Flask app on Webfaction
    http://flask.pocoo.org/snippets/65/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


"""
Webfaction is a Python friendly hosting with affordable pricing and tons of useful features.

To deploy a Flask application on Webfaction you should follow these steps:

Create an application in Webfaction control panel choosing "mod_wsgi 3.2/Python 2.6" or another one of the available Python version.
The system will automagically create some folder under the webapps directory in your home folder
webapps/yourapplication/
|-- apache2
|   |-- bin
|   |-- conf
|   |-- lib
|   |-- logs
|   `-- modules
`-- htdocs
Install Flask and all the extensions you need using easy_install:
foo@bar:~$ easy_install-2.6 Flask
Note that Webfaction gives you different easy_install executables: use the one that meets the Python version you choose when the application was created.

Open webapps/yourapp/index.py delete the content and add the following line:
from yourapp import app as application
Modify your webapps/yourapp/apache2/conf/httpd.conf. At the bottom of the file add the following lines changing yourapp and yourusername according to your setup:
WSGIPythonPath /home/yourusername/webapps/yourapp/htdocs/
#If you do not specify the following directive the app *will* work but you will
#see index.py in the path of all URLs
WSGIScriptAlias / /home/yourusername/webapps/yourapp/htdocs/index.py

<Directory /home/yourusername/webapps/yourapp/htdocs/>
   AddHandler wsgi-script .py
   RewriteEngine on
   RewriteBase /
   WSGIScriptReloading On
</Directory>
If you have choosed / as the mout point for your application you are done. If you mounted the application somewhere else (i.e. /blog) there is some additional work to do.

You need to write a WSGI middleware that prefixes SCRIPT_NAME with that prefix otherwise the url_for function will not be able to create the correct URLs for you (the following snippets is kindly provided by Armin himself).

class WebFactionMiddleware(object):
    def __init__(self, app):
        self.app = app
    def __call__(self, environ, start_response):
        environ['SCRIPT_NAME'] = '/yourapp'
        return self.app(environ, start_response)

app.wsgi_app = WebFactionMiddleware(app.wsgi_app)
You can put this snippet in the application's __init__.py.

Happy Flasking!
"""


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
