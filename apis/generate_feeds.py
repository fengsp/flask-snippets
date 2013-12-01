# -*- coding: utf-8 -*-
"""
    apis.generate_feeds
    ~~~~~~~~~~~~~~~~~~~

    Generating Feeds with Flask
    http://flask.pocoo.org/snippets/10/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from urlparse import urljoin

from flask import request, Response
from werkzeug.contrib.atom import AtomFeed

from app import app


def make_external(url):
    return urljoin(request.url_root, url)


@app.route('/recent.atom')
def recent_feed():
    feed = AtomFeed('Recent Articles', 
                    feed_url=request.url, url=request.url_root)
    articles = Article.query.order_by(Article.pub_date.desc()) \
                          .limit(15).all()
    for article in articles:
        feed.add(article.title, unicode(article.rendered_text),
                 content_type='html',
                 author=article.author.name,
                 url=make_external(article.url),
                 updated=article.last_update,
                 published=article.published)
    return feed.get_response()


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
