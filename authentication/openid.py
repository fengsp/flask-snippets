# -*- coding: utf-8 -*-
"""
    authentication.openid
    ~~~~~~~~~~~~~~~~~~~~~

    Simple OpenID with Flask
    http://flask.pocoo.org/snippets/7/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


"""
There is a Flask Addon Library called Flask-OpenID that implements basic OpenID authentication for Flask on top of python-openid.

The included example shows how this can be done. Basically all you need to do is this:

create an instance of OpenID with the path to the stored files. This can be any folder on the filesystem, OpenID will use it to store temporary information required for the authentication process.
Define a loginhandler function. That function has to render the form and call into try_login with the submitted identity URL (the OpenID the user entered).
Define a after_login function. This function is called with the identity URL if authentication worked. This function must redirect to a different page. It usually checks if the user is known to the system and if this is the case, logs the user in or otherwise redirects to a page used to create that profile.
If that is too abstract, look at the example for more information about how to use it.

Note that Flask-OpenID also has basic support for redirections, so the user will after login end up on the page where he or she previously was. For the redirections to work, it is necessary to have the forms forward the next parameter properly. Make sure to have a look at the template code as well.

Also check out the website for more information and a detailed documentation: Flask-OpenID
"""


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
