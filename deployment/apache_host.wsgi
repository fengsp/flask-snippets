# -*- coding: utf-8 -*-
import sys, os
sys.path.insert(0, '/var/www/myapp')
os.chdir("/var/www/myapp")
from srv import app as application
