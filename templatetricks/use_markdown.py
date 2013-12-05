# -*- coding: utf-8 -*-
"""
    templatetricks.use_markdown
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Using the markdown language
    http://flask.pocoo.org/snippets/19/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import render_template_string, Markup
import markdown

from app import app


html_content = """
<html>
  <head>
    <title>Markdown Snippet</title>
  </head>
  <body>
    {{ content }}
  </body>
</html>
"""


@app.route('/')
def index():
    content = """
Chapter
=======

Section
-------

* Item 1
* Item 2
"""
    content = Markup(markdown.markdown(content))
    return render_template_string(html_content, **locals())


if __name__ == "__main__":
    app.run()
