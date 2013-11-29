# -*- coding: utf-8 -*-
"""
    urls.generate_map
    ~~~~~~~~~~~~~~~~~

    Generating a sitemap.xml
    http://flask.pocoo.org/snippets/108/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app



@sk-sqlalchemy model for User
class User(db.Model, UserMixin):

    __tablename__ = 'users'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(32), nullable=False, unique=True)
    email = Column(db.String, nullable=False, unique=True)
    activation_key = Column(db.String)
    created_time = Column(db.DateTime, default=get_current_time)
    modified_time = Column(db.TIMESTAMP, onupdate=get_current_time(), default=get_current_time())


# a route for generating sitemap.xml
@frontend.route('/sitemap.xml', methods=['GET'])
def sitemap():
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=datetime.now() - timedelta(days=10).date().isoformat()
      # static pages
      for rule in current_app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0:
              pages.append(
                           [rule.rule,ten_days_ago]
                           )
      
      # user model pages
      users=User.query.order_by(User.modified_time).all()
      for user in users:
          url=url_for('user.pub',name=user.name)
          modified_time=user.modified_time.date().isoformat()
          pages.append([url,modified_time]) 

      sitemap_xml = render_template('frontend/sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"    
    
      return responseapp.route('/')


"""
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {% for page in pages %}
    <url>
        <loc>{{page[0]|safe}}</loc>
        <lastmod>{{page[1]}}</lastmod>
    </url>
    {% endfor %}
</urlset>
"""


def index():
    return 'index'


if __name__ == "__main__":
    app.run()
