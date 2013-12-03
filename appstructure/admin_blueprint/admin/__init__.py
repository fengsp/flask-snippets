# -*- coding: utf-8 -*-
from flask import Blueprint
from flask import redirect, request
from google.appengine.api import users

bp = Blueprint('admin', __name__)

@bp.before_request
def restrict_bp_to_admins():
    if not users.is_current_user_admin():
        return redirect(users.create_login_url(request.url))
