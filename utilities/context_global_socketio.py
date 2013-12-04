# -*- coding: utf-8 -*-
"""
    utilities.cms_pages
    ~~~~~~~~~~~~~~~~~~~

    CMS Pages
    http://flask.pocoo.org/snippets/114/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template_string

from app import app


class Page(Base):
    __tablename__='pages'
    id Column(Integer, primary_key=True)
    name = Column(String())
    page_snippets = relationship('PageSnippets', backref='pages', lazy='dynamic')


class PageSnippets('base')
    __tablename__='page_snippets'
    id Column(Integer, primary_key=True)
    snippet = Column(String())
    language = Column(String())


html_content = """
<p>{{page_snippets.intro}}</b>
<div class="footer">
<p>{{page_snippets.footer}}
</div>
"""


@app.route('/<page_id>')
def a_page(page_id):
    page = Page.query.filter_by(id=page_id).one()
    page_snippets = page.page_snippets
    return render_template_string(html_content, page_snippets=page_snippets)
