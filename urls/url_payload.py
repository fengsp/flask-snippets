# -*- coding: utf-8 -*-
"""
    urls.url_payload
    ~~~~~~~~~~~~~~~~

    URLs with Payload
    http://flask.pocoo.org/snippets/50/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response
from flask import abort, redirect, flash, url_for
from itsdangerous import URLSafeSerializer, BadSignature

from app import app


def get_serializer(secret_key=None):
    if secret_key is None:
        secret_key = app.secret_key
    return URLSafeSerializer(secret_key)


def get_activation_link(user):
    s = get_serializer()
    payload = s.dumps(user.id)
    return url_for('activate_user', payload=payload, _external=True)


@app.route('/users/activate/<payload>')
def activate_user(payload):
    s = get_serializer()
    try:
        user_id = s.loads(payload)
    except BadSignature:
        abort(404)

    # user = User.query.get_or_404(user_id)
    # user.activate()
    flash('User activated')
    return redirect(url_for('index'))


@app.route('/')
def index():
    return 'index'


@app.route('/voucher/redeem/<payload>')
def redeem_voucher(payload):
    s = get_serializer()
    try:
        user_id, voucher_id = s.loads(payload)
    except BadSignature:
        abort(404)

    user = User.query.get_or_404(user_id)
    voucher = Voucher.query.get_or_404(voucher_id)
    voucher.redeem_for(user)
    flash('Voucher redeemed')
    return redirect(url_for('index'))

def get_redeem_link(user, voucher):
    s = get_serializer()
    payload = s.dumps([user.id, voucher.id])
    return url_for('redeem_voucher', payload=payload, 
                   _external=True)


if __name__ == "__main__":
    ctx = app.test_request_context()
    ctx.push()
    class User(object):
        id = 10000
    user = User()
    print get_activation_link(user)
