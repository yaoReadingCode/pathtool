#!/usr/bin/env python
# encoding: utf-8
"""
pathtool-cli.py 0.1

A commandline tool for walking a filesystem.
Takes Action callback plugins in a plugin directory

action=(lambda rec: print_rec(rec))

"""

from pathtool import path
import optparse
import re
import os
import sys

try:
    plugin_available = True
    from plugin import *
    from plugin import __all__ #note this is the registered plugin list
except ImportError:
    plugin_available = False
        
def path_controller():
    descriptionMessage = """
    A command line tool for walking a filesystem.\
    Takes callback 'Action' functions as plugins.\
    
    example: pathtool_cli /tmp print_path_ext
    """
    p = optparse.OptionParser(description=descriptionMessage,
                                prog='pathtool',
                                version='pathtool 0.1.1',
                                usage= '%prog [starting directory][action]')
    p.add_option('--pattern', '-p',
                help='Pattern Match Examples: *.txt, *.iso, music[0-5].mp3\
                plain number defaults to * or match all.  \
                Uses UNIX standard wildcard syntax.',
                default='*')

    p.add_option('--list', '-l',
            action="store_true",
            help='lists available action plugins',
            default=False)
                    
    options, arguments = p.parse_args()
    if options.list:
        try:
            print "Action Plugins Available:"
            if plugin_available:
                for p in __all__:
                    print p
        finally:
            sys.exit(0)
            
    if len(arguments) == 2:
        fullpath = arguments[0]
        try:
            action_plugin = eval(arguments[1])   
            #note we expect the plugin author to write a method with our naming convention
            #path(fullpath,options.pattern,action=(lambda rec: move_to_tmp.plugin(rec)))
            path(fullpath, options.pattern,action=(lambda rec: action_plugin.plugin(rec)))
        except NameError:
            sys.stderr.write("Plugin Not Found")
            sys.exit(1)
    else:
        print p.print_help()

def main():
    path_controller()

if __name__ == '__main__':
    main()

