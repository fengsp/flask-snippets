# -*- coding: utf-8 -*-
"""
    javascript.push
    ~~~~~~~~~~~~~~~

    Push Notifications with socket.io and Juggernaut
    http://flask.pocoo.org/snippets/80/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request
from juggernaut import Juggernaut

from app import app


"""
    $ npm install -g juggernaut
    $ juggernaut
    $ pip install juggernaut

    <script type=text/javascript src=http://localhost:8080/application.js></script>
    <script type=text/javascript>
        var jug = new Juggernaut();
        jug.subscribe('channel', function(data) {
            alert('Got message: ' + data);
        });
    </script>
"""


@app.route('/')
def index():
    return 'index'


@app.route('/publish/')
def publish():
    jug = Juggernaut()
    jug.publish('channel', 'The message')


if __name__ == "__main__":
    app.run()
