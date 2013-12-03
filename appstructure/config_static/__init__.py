# -*- coding: utf-8 -*-
"""
    appstructure.config_static
    ~~~~~~~~~~~~~~~~~~~~~~~~~~

    Config-based static_folder
    http://flask.pocoo.org/snippets/102/
"""

import flask


class MyFlask(flask.Flask):
    @property
    def static_folder(self):
        if self.config.get('STATIC_FOLDER') is not None:
            return os.path.join(self.root_path,
                self.config.get('STATIC_FOLDER'))
    @static_folder.setter
    def static_folder(self, value):
        self.config.get('STATIC_FOLDER') = value


# Now these are equivalent:
app = Flask(__name__, static_folder='foo')


app = MyFlask(__name__)
app.config['STATIC_FOLDER'] = 'foo'
