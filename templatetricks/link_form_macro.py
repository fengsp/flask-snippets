# -*- coding: utf-8 -*-
"""
    templatetricks.link_form_macro
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    link_to and form_tag macros
    http://flask.pocoo.org/snippets/14/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from app import app


"""
The HTML/Jinja for a link to a page on your site looks quite awkward.

<a href="{{ url_for('some.view', foo='bar') }}">Link text!</a>
With this macro:

{% macro link_to(endpoint, text) -%}
<a href="{{ url_for(endpoint, **kwargs) }}">{{ text|safe }}</a>
{%- endmacro %}
The above link will become:

{{ link_to('some.view', "Link text!", foo=bar) }}
It's shorter and looks cleaner, especially if the content of the link is also a variable.

A similar technique, using the call tag, can be used for forms:

{% macro form_tag(endpoint, method='post') -%}
<form action="{{ url_for(endpoint, **kwargs) }}" 
      method="{{ method }}">
  {{ caller () }}
</form>
{%- endmacro %}
Then, you can create a form with:

{% call form_tag('create_entry') %}
<p><input type=text name=whatever></p>

<p><input type=submit value=Submit></p>
{% endcall %}
"""
