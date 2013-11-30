# -*- coding: utf-8 -*-
"""
    deployment.dotcloud
    ~~~~~~~~~~~~~~~~~~~

    Deploying a Flask app on Dotcloud
    http://flask.pocoo.org/snippets/48/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


"""
How to deploy a Flask app on Dotcloud
Create the namespace you want:

dotcloud create <namespace>
A DotCloud application is described by a build file, which is a simple YAML file named "dotcloud.yml" located in your local source directory. To add a new python service to your app, just add the following lines to <source_folder>/dotcloud.yml:

www:
  type: python
Now create a <source_folder>/wsgi.py file containing:

import sys
sys.path.append('/home/dotcloud/current')
from <your_app_package> import app as application
/home/dotcloud/current is the default path to your app on the server.

Eventually, create nginx.conf and uwsgi.conf in the source folder. See Dotcloud documentation for further information.

Create your requirements.txt file:

pip freeze > ./requirements.txt
Now, make sure that your source folder contains at least:

./
../
./<your_app_package>
    ./static
    ./__init__.py
    ./ ...
./requirements.txt
./wsgi.py
./dotcloud.yml
./ ...
Create a symbolic link to your static folder:

cd <source_folder>
ln -s <your_app_package>/static static
You can now push the code to Dotcloud:

dotcloud push <namespace>
A random URL has been generated for your python service in your application (something like http://my4ppr0x.dotcloud.com/). Point your browser to this URL to see your new app running.
"""


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
