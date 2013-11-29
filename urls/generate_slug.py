# -*- coding: utf-8 -*-
"""
    urls.generate_slug
    ~~~~~~~~~~~~~~~~~~

    Generating Slugs
    http://flask.pocoo.org/snippets/5/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import re
from unicodedata import normalize

from flask import request, Response
#from unidecode import unidecode

from app import app


_punct_re = re.compile(r'[\t !"#$%&\'()*\-/<=>?@\[\\\]^_`{|},.]+')


def slugify(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = word.encode('translit/long')
        if word:
            result.append(word)
    return unicode(delim.join(result))


def slugify2(text, delim=u'-'):
    """Generates an slightly worse ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        word = normalize('NFKD', word).encode('ascii', 'ignore')
        if word:
            result.append(word)
    return unicode(delim.join(result))


def slugify3(text, delim=u'-'):
    """Generates an ASCII-only slug."""
    result = []
    for word in _punct_re.split(text.lower()):
        result.extend(unidecode(word).split())
    return unicode(delim.join(result))


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    # print slugify('Hello World')
    # print slugify('ü')
    print slugify2(u'Hello World')
    print slugify2(u'ü')
    app.run()
