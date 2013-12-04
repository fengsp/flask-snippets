# -*- coding: utf-8 -*-
"""
    utilities.interactive_shell
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Preconfigured interactive shell
    http://flask.pocoo.org/snippets/23/
"""

import os
import readline
from pprint import pprint

from flask import *

from myapp import *
from utils import *
from db import *
from models import *


os.environ['PYTHONINSPECT'] = 'True'
