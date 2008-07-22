#!/usr/bin/env python
# encoding: utf-8
"""
pathtool.py 0.1.1 alpha

Created by Noah Gift on 2008-07-13.
Copyright (c) MIT License. All rights reserved.

A generator based toolkit for walking a filesystem
The API is pretty simple:

Just call the path function and pass it full path, and optionally a filter, and action callback
Example:

from pathtool import path

path("/tmp", pattern=".mp3")

This would print all the .mp3 files.  If you assign a callback to the action, you could
then do something like create a tar archive of each file.  Alternately you could check
the unique_id value of each record and perform an action based on that.  

A callback takes this form:

action = (lambda rec: print_rec(rec))

so a new callback would create a function that used the rec dictionary below:

rec = {"path": path, "filename": file, "ext": ext, "size": size,
                "unique_id": unique_id, "mtime": mtime, "ctime": ctime}
                
And then it would be called as follows:

path("/foo", pattern".mov", action=(lambda rec: convert_to_quicktime(rec)))                

This would presume that a plugin or function was created that converted 
.mov files to quicktime.



"""
import os
import fnmatch
import hashlib
import time
import shutil

global_session_unique_id = {}   #global id cache for each session, needs to be set

def checksum(fullpath):
    """Reads in file, performs checksum and yields checksum"""
    try:    
        fp = open(fullpath)
        checksum = hashlib.md5()
        while True:
            buffer = fp.read(8192)
            if not buffer: break
            checksum.update(buffer)
        fp.close()
        checksum = checksum.digest()
    except IOError:
        return None    
    return checksum
        
def pathname(fullpath):
    """Gets just pathname and yields it"""
    for root, directory, filename in os.walk(fullpath):
        for file in filename:
            yield os.path.join(root, file)

def extension(filename):
    """Takes filename and returns extension or None"""
    (shortname, ext) = os.path.splitext(filename)
    if file == ext: 
        return None
    return ext

def unique_id_func(size, fullpath, gid=False):
    """Create uniqueness dict
    
    Alternately, the value of the unique set can be either None,
    True, or False.  If it is None, then the global session has not
    been set.  If it is True, then the unique_set has already been found
    in the global session cache, if it False, then the unique_set has not been found in
    this global session cache so far.
    """
    hash_value = checksum(fullpath)
    unique_set = (size, hash_value)
    if gid:
        if unique_set in global_session_unique_id:
            return {unique_set:True}
        else:
             return {unique_set:False}   
    return {unique_set:None}
    
def pathattr(fullpath, gid=False):
    """Gets fullpath of files in a directory and yields a collection of useful values
    
    If set_global_id is to True then the unique_id set populates the global_file_unique_id
    dictionary.  This is used if you need to find global uniqueness or a file in a session.
    """
    for root, directory, filename in os.walk(fullpath):
        for file in filename:
            try:
                path = os.path.join(root, file)  
                ext = extension(file)
                size = os.path.getsize(path) 
                unique_id = unique_id_func(size,path,gid)                
                mtime = time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getmtime(path)))
                ctime = time.strftime("%m/%d/%Y %I:%M:%S %p",time.localtime(os.path.getctime(path)))
                path_attributes = {"path": path, "filename": file, "ext": ext, "size": size,
                "unique_id": unique_id, "mtime": mtime, "ctime": ctime}
            except OSError:
                yield {"path": None, "filename": None, "ext": None, "size": None,
                "unique_id": None, "mtime": None, "ctime": None}
            yield path_attributes
                        
def match(pattern,rec):
    """Takes a dictionary of file attributes, and a pattern
        yields "filtered" dictionary back
    """
    name = rec["filename"]
    if name != None:
        if fnmatch.fnmatch(name, pattern):
            yield rec
        
def print_rec(rec):
    """A default action that prints path from a file attributes dictionary"""
    print rec["path"]
        
def path(fullpath, pattern="*", action=(lambda rec: print_rec(rec))):
    """This takes a path, a shell pattern, and an action callback
    This function uses the slower pathattr function which calculates checksums
    """
    for rec in pathattr(fullpath):
        for new_record in match(pattern, rec):  #applies filter
            action(new_record)  #Applies lambda callback to generator object 

def dtest():
    import doctest  
    doctest.testmod(verbose=True)    

def main():
    dtest()
if __name__ == '__main__':
    main()

