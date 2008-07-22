#!/usr/bin/env python
# encoding: utf-8
"""
prints path, name, ext, plugin
"""

def plugin(rec, verbose=True):
    """Moves matched files to tmp directory"""
    path = rec["path"]
    filename = rec["filename"]
    ext = rec["ext"]
    print "%s | %s | %s" % (path, filename, ext)
