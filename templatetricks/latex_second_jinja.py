# -*- coding: utf-8 -*-
"""
    templatetricks.latex_second_jinja
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Using a second Jinja environment for LaTeX templates.
    http://flask.pocoo.org/snippets/55/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response, render_template, redirect, url_for

from app import app


LATEX_SUBS = (
    (re.compile(r'\\'), r'\\textbackslash'),
    (re.compile(r'([{}_#%&$])'), r'\\\1'),
    (re.compile(r'~'), r'\~{}'),
    (re.compile(r'\^'), r'\^{}'),
    (re.compile(r'"'), r"''"),
    (re.compile(r'\.\.\.+'), r'\\ldots'),
)

def escape_tex(value):
    newval = value
    for pattern, replacement in LATEX_SUBS:
        newval = pattern.sub(replacement, newval)
    return newval

texenv = app.create_jinja_environment()
texenv.block_start_string = '((*'
texenv.block_end_string = '*))'
texenv.variable_start_string = '((('
texenv.variable_end_string = ')))'
texenv.comment_start_string = '((='
texenv.comment_end_string = '=))'
texenv.filters['escape_tex'] = escape_tex


template = texenv.get_template('template.tex')
template.render(name='Tom')


"""
\documentclass{article}

\begin{document}
Hello, ((( name|escape_tex )))!
\end{document}
"""
