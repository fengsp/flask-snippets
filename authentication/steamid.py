# -*- coding: utf-8 -*-
"""
    authentication.steamid
    ~~~~~~~~~~~~~~~~~~~~~~

    Sign in with Steam ID
    http://flask.pocoo.org/snippets/42/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import re
import urllib2

from flask import Flask, redirect, session, json, g
from flaskext.sqlalchemy import SQLAlchemy
from flaskext.openid import OpenID

from app import app


app.config['STEAM_API_KEY'] = 'ABCDEFG-12345'
db = SQLAlchemy(app)
oid = OpenID(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    steam_id = db.Column(db.String(40))
    nickname = db.String(80)

    @staticmethod
    def get_or_create(steam_id):
        rv = User.query.filter_by(steam_id=steam_id).first()
        if rv is None:
            rv = User()
            rv.steam_id = steam_id
            db.session.add(rv)
        return rv


def get_steam_userinfo(steam_id):
    options = {
        'key': app.config['STEAM_API_KEY'],
        'steamids': steam_id
    }
    url = 'http://api.steampowered.com/ISteamUser/' \
          'GetPlayerSummaries/v0001/?%s' % url_encode(options)
    rv = json.load(urllib2.urlopen(url))
    return rv['response']['players']['player'][0] or {}


_steam_id_re = re.compile('steamcommunity.com/openid/id/(.*?)$')


@app.route('/login')
@oid.loginhandler
def login():
    if g.user is not None:
        return redirect(oid.get_next_url())
    return oid.try_login('http://steamcommunity.com/openid')


@oid.after_login
def create_or_login(resp):
    match = _steam_id_re.search(resp.identity_url)
    g.user = User.get_or_create(match.group(1))
    steamdata = get_steam_userinfo(g.user.steam_id)
    g.user.nickname = steamdata['personaname']
    db.session.commit()
    session['user_id'] = g.user.id
    flash('You are logged in as %s' % g.user.nickname)
    return redirect(oid.get_next_url())


@app.before_request
def before_request():
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(oid.get_next_url())


if __name__ == "__main__":
    app.run()
