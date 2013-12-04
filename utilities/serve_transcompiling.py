# -*- coding: utf-8 -*-
"""
    utilities.serve_transcompiling
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    Serve CoffeeScript, SCSS, or other transcompiling file via Python
    http://flask.pocoo.org/snippets/90/
"""

from subprocess import Popen, PIPE
import shlex

class NonZeroExitError(Exception):
    def __init__(self, command, returncode, output, error):
        self.command = command
        self.returncode = returncode
        self.output = output
        self.error = error
    def __str__(self):
        return '''\
        %s returned non-zero exit status %d with output
        %s
        and error
        %s''' % (self.command, self.returncode,
                 self.output or "[NO OUTOUT]",
                 self.error or "[NO ERROR]")

def command_line_renderer_factory(command):
    '''command should be a command reads input from stdin
    and prints to stdout'''
    
    args = shlex.split(command)
    
    def renderer(script):
        '''Accepts a file object or path and return the
        rendered string'''
        
        if isinstance(script, file):
            pass
        elif isinstance(script, str):
            script = open(script)
        else:
            raise TypeError('script must be a file object of '
                            'or a string to the file')
        process = Popen(args, stdin=script,
                        stdout=PIPE, stderr=PIPE)
        
        returncode = process.wait()
        stdoutdata, stderrdata = process.communicate()
        
        if returncode != 0:
            raise NonZeroExitError(command, returncode,
                                   stdoutdata, stderrdata)
        
        return stdoutdata
    
    return renderer


"""
#!/usr/bin/env node

var less = require('less');

process.stdin.resume();
process.stdin.setEncoding('utf8');

process.stdin.on('data', function (less_css) {
  less.render(less_css, function(e, css){
    console.log(css)
  });
});
"""
