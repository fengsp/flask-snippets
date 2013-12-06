# -*- coding: utf-8 -*-
"""
    database.lazy_sqlalchemy
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Lazy SQLAlchemy setup
    http://flask.pocoo.org/snippets/22/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, create_session


engine = None


db_session = scoped_session(lambda: create_session(bind=engine))


def init_engine(uri, **kwargs):
    global engine
    engine = create_engine(uri, **kwargs)
    return engine


def create_app(config):
    
    app = Flask(__name__)
    app.config.from_pyfile(config)
    
    init_engine(app.config['DATABASE_URI'])
    
    return app
