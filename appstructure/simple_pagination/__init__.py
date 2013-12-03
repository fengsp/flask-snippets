# -*- coding: utf-8 -*-
"""
    appstructure.simple_pagination
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Simple Pagination
    http://flask.pocoo.org/snippets/44/
"""
from math import ceil


class Pagination(object):

    def __init__(self, page, per_page, total_count):
        self.page = page
        self.per_page = per_page
        self.total_count = total_count

    @property
    def pages(self):
        return int(ceil(self.total_count / float(self.per_page)))

    @property
    def has_prev(self):
        return self.page > 1

    @property
    def has_next(self):
        return self.page < self.pages

    def iter_pages(self, left_edge=2, left_current=2,
                   right_current=5, right_edge=2):
        last = 0
        for num in xrange(1, self.pages + 1):
            if num <= left_edge or \
               (num > self.page - left_current - 1 and \
                num < self.page + right_current) or \
               num > self.pages - right_edge:
                if last + 1 != num:
                    yield None
                yield num
                last = num


def url_for_other_page(page):
    args = request.view_args.copy()
    args['page'] = page
    return url_for(request.endpoint, **args)
app.jinja_env.globals['url_for_other_page'] = url_for_other_page


from flask import redirect

PER_PAGE = 20

@app.route('/users/', defaults={'page': 1})
@app.route('/users/page/<int:page>')
def show_users(page):
    count = count_all_users()
    users = get_users_for_page(page, PER_PAGE, count)
    if not users and page != 1:
        abort(404)
    pagination = Pagination(page, PER_PAGE, count)
    return render_template('users.html',
        pagination=pagination,
        users=users
    )


"""
{% macro render_pagination(pagination) %}
  <div class=pagination>
  {%- for page in pagination.iter_pages() %}
    {% if page %}
      {% if page != pagination.page %}
        <a href="{{ url_for_other_page(page) }}">{{ page }}</a>
      {% else %}
        <strong>{{ page }}</strong>
      {% endif %}
    {% else %}
      <span class=ellipsis>…</span>
    {% endif %}
  {%- endfor %}
  {% if pagination.has_next %}
    <a href="{{ url_for_other_page(pagination.page + 1)
      }}">Next &raquo;</a>
  {% endif %}
  </div>
{% endmacro %}
"""
