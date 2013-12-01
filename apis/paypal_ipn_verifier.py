# -*- coding: utf-8 -*-
"""
    apis.paypal_ipn_verifier
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Paypal IPN Verifier for Flask
    http://flask.pocoo.org/snippets/112/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from flask import request, Response

from app import app


IPN_URLSTRING = 'https://www.sandbox.paypal.com/cgi-bin/webscr'
IPN_VERIFY_EXTRA_PARAMS = (('cmd', '_notify-validate'),)
from itertools import chain


def ordered_storage(f):
    import werkzeug.datastructures
    import flask
    def decorator(*args, **kwargs):
        flask.request.parameter_storage_class = werkzeug.datastructures.ImmutableOrderedMultiDict
        return f(*args, **kwargs)
    return decorator


@app.route('/paypal/', methods=['POST'])
@ordered_storage
def paypal_webhook():
    #probably should have a sanity check here on the size of the form data to guard against DoS attacks
    verify_args = chain(request.form.iteritems(), IPN_VERIFY_EXTRA_PARAMS)
    verify_string = '&'.join(('%s=%s' % (param, value) for param, value in verify_args))
    #req = Request(verify_string)
    response = urlopen(IPN_URLSTRING, data=verify_string)
    status = response.read()
    print status
    if status == 'VERIFIED':
        print "PayPal transaction was verified successfully."
        # Do something with the verified transaction details.
        payer_email =  request.form.get('payer_email')
        print "Pulled {email} from transaction".format(email=payer_email)
    else:
         print 'Paypal IPN string {arg} did not validate'.format(arg=verify_string)

    return jsonify({'status':'complete'})


@app.route('/')
def index():
    return 'index'


if __name__ == "__main__":
    app.run()
