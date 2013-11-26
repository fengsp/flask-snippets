# -*- coding: utf-8 -*-
"""
    decorators.view_render
    ~~~~~~~~~~~~~~~~~~~~~~

    View Rendering Decorator
    http://flask.pocoo.org/snippets/18/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from werkzeug import BaseResponse

from app import app


def render_html(template, **defaults):
    def wrapped(result):
        variables = defaults.copy()
        variables.update(result)
        return render_template(template, **variables)
    return wrapped


def view(self, url, renderer=None, *args, **kwargs):
    super_route = self.route

    defaults = kwargs.pop('defaults', {})
    route_id = object()
    defaults['_route_id'] = route_id

    def deco(f):
        @super_route(url, defaults=defaults, *args, **kwargs)
        @wraps(f)
        def decorated_function(*args, **kwargs):
            this_route = kwargs.get('_route_id')
            if not getattr(f, 'is_route', False):
                del kwargs['_route_id']

            result = f(*args, **kwargs)

            if this_route is not route_id:
                return result

            # catch redirects.
            if isinstance(result, (app.response_class,
                                   BaseResponse)):
                return result

            if renderer is None:
                return result
            return renderer(result)

        decorated_function.is_route = True
        return decorated_function

    return deco


@view(app, '/<name>', render_html('page.html'))
def show_page(name):
    page = load_page(name)
    return dict(title=page.title, contents=page.contents)


if __name__ == "__main__":
    app.run()
