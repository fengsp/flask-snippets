# -*- coding: utf-8 -*-
"""
    javascript.timeago_filter
    ~~~~~~~~~~~~~~~~~~~~~~~~~

    A Filter for the jQuery Timeago Plugin
    http://flask.pocoo.org/snippets/49/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


"""
Timeago is a jQuery plugin that makes it easy to support automatically 
updating fuzzy timestamps (e.g. “4 minutes ago” or “about 1 day ago”). 
It automatically keeps them updated and only needs a very basic span 
tag or something similar with a certain class and title attribute.
    
For instance
    <span class=timeago title="2008-07-17T09:24:17Z">...</span>
turns into something like this:
    <span class=timeago title="July 17, 2008">2 years ago</span>
"""


@app.template_filter()
def datetimeformat(datetime, timeago=True):
    readable = datetime.strftime('%Y-%m-%d @ %H:%M')
    if not timeago:
        return readable
    iso_format = datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
    return '<span class=timeago title="%s">%s</span>' % (
        iso_format,
        readable
    )


"""
Usage:
    <p class=date>Date: {{ the_date|datetimeformat }}

    $(function() {
        $('span.timeago').timeago();
    });
"""


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
