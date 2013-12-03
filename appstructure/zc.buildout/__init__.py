# -*- coding: utf-8 -*-
"""
    appstructure.zc.buildout
    ~~~~~~~~~~~~~~~~~~~~~~~~

    Deploy using zc.buildout and PythonPaste
    http://flask.pocoo.org/snippets/27/
"""

"""
Deploy the application
First, you could save the buildout directory using your favorite DVCS, or create a tarball for future deployments.

Then bootstrap the buildout:

~/buildout_env $ python bootstrap.py --distribute
Adjust your settings in buildout.cfg, and build the application:

~/buildout_env $ bin/buildout
Run the tests:

~/buildout_env $ bin/test
Test rendered page. ... ok

------------------------------------------------------------
Ran 1 test in 0.055s

OK
~/buildout_env $ 
Now launch the server:

~/buildout_env $ bin/flask-ctl debug fg
bin/paster serve parts/etc/debug.ini --reload
Starting subprocess with file monitor
Starting server in PID 24862.
serving on http://127.0.0.1:5000
Visit http://127.0.0.1:5000 with your browser.
Visit http://127.0.0.1:5000/?broken to bring the Werkzeug Debugger. Quit the application with Ctrl+C.

Note: when you change the configuration in buildout.cfg, you need to rebuild the application using bin/buildout.

Further reading:

http://www.buildout.org
http://pythonpaste.org

"""
