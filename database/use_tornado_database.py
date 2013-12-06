# -*- coding: utf-8 -*-
"""
    database.use_tornado_database
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Using tornado.database with MySQL
    http://flask.pocoo.org/snippets/11/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from tornado.database import Connection
from flask import g, render_template

from app import app
import config


@app.before_request
def connect_db():
    g.db = Connection(config.DB_HOST,
                      config.DB_NAME,
                      config.DB_USER,
                      config.DB_PASSWD)


@app.after_request
def close_connection(response):
    g.db.close()
    return response


@app.route("/")
def index():
    newsitems = g.db.iter("select * from newsitems")
    return render_template("index.html", newsitems=newsitems)


"""
{% for item in newsitems %}
<h3>{{ item.title }}</h3>
{% endfor %}
You can get much of the same functionality in SQLAlchemy 0.6 using NamedTuples, without using the ORM:

from sqlalchemy import create_engine

@app.before_request
def connect_db():
    g.db = create_engine(config.DB_URI)

@app.route("/")
def index():
    newsitems = g.db.execute("select * from newsitems")
    # now you can do newsitem.title... 
"""
