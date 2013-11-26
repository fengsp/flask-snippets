# -*- coding: utf-8 -*-
"""
    decorators.before_request_for_coffeescript
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    app.before_request handlers for less and coffeescript
    http://flask.pocoo.org/snippets/94/
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from functools import wraps

from app import app


def _simple_processor(processor, ext_private, ext_public):
    if not request.path.endswith(ext_public):
        return
    public_file = request.path[len(config.app.static_url_path) + 1:]
    public_file_path = os.path.join(config.app.static_folder, public_file)
    private_file_path = public_file_path[:-len(ext_public)] + ext_private
    # File does not exist in app static - check blueprints.
    if not os.path.isfile(private_file_path):
        for blueprint_name, blueprint in config.app.blueprints.iteritems():
            if request.path.startswith(blueprint.static_url_path):
                public_file = request.path[len(blueprint.static_url_path) + 1:]
                public_file_path = os.path.join(blueprint.static_folder, public_file)
                private_file_path = public_file_path[:-len(ext_public)] + ext_private
                break
    # If file doesn't exist in the blueprints as well, let flask handle it.
    if not os.path.isfile(private_file_path):
        return
    if not os.path.isfile(public_file_path) or (os.path.getmtime(private_file_path) >=
                                                os.path.getmtime(public_file_path)):
        processor(private_file_path, public_file_path)

@app.before_request
def less_to_css():
    processor = lambda in_file, out_file: subprocess.check_output(['lessc',
                                                                   in_file, out_file], shell=False)
    return _simple_processor(processor, '.less', '.css')

@app.before_request
def coffee_to_js():
    processor = lambda in_file, out_file: subprocess.check_output(['coffee',
                                                                   '-c', in_file], shell=False)
    return _simple_processor(processor, '.coffee', '.js')
