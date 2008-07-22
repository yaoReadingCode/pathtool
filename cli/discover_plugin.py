#!/usr/bin/env python
# encoding: utf-8
"""
discover_plugin.py

Created by ngift on 2008-07-20.
Copyright (c) 2008 __MyCompanyName__. All rights reserved.
"""

import sys
import os

def get_plugin():
    """Imports Plugins"""
    
    #registered_plugins
    registered_plugins = []

    #check to see if a plugins directory exists
    plugin_dir = "%s/plugin" % os.getcwd()
    if os.path.exists(plugin_dir):
        plugins = os.listdir(plugin_dir)
        pattern = ".py$"
    
        #register .py files
        for plugin in plugins:
            if plugin != "__init__.py":
                if re.search(pattern, plugin):
                    (shortname, ext) = os.path.splitext(plugin)
                    #print shortname
                    registered_plugins.append(shortname)
    return registered_plugins

def main():
	pass


if __name__ == '__main__':
	main()

