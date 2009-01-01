"""
Pathtool 0.2

Object-Oriented Generator based Python Path API

This is unique API because it combines the efficiency of generators
and the power of Objects.

"""

import os
import time

class BaseOb():
    """Base Class to inhert attributes about files, directories, and tree"""

    def __init__(self, name = None,
                    abspath = None,
                    relpath = None,
                    modified = None,
                    created = None,
                    accessed = None,
                    size = None,
                    symbolic = None):

            self.name = name
            self.abspath = abspath
            self.relpath = relpath
            self.modified = modified
            self.created = created
            self.size = size
            self.symbolic = None

class FileOb(BaseOb):

    """Holds extended information about files.

    Note, not all of these attributes need to be filled out, for example,
    it could be quite expensive to always calculate a hash, but it is a place
    holder that can be filled in as necessary.

    """
    def __init__(self, ext = None, hash = None):
        BaseOb.__init__(self)
        self.ext = ext
        self.hash = hash

class DirOb(BaseOb):

    """Holds extended information about a directory"""

    def __init__(self, name = None, members = None, file_count = None):
        BaseOb.__init__(self)
        self.members = members #FileOb instances
        self.file_count = file_count

class TreeOb(BaseOb):

    """Holds extended information about a directory tree"""

    def __init__(self):
        BaseOb.__init__(self)

class FileAttrHelper():

    """Helper class creating attributes for FileOb instances"""

    def extension(self, filename):
        """Takes filename and returns extension or None"""

        (shortname, ext) = os.path.splitext(filename)
        if file == ext:
            return None
        return ext

    def checksum(self, path):
        """Reads in file, performs checksum and yields checksum"""
        
        try:
            fp = open(path)
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
    
    def mtime(self, path):
        """Gets modified time"""

        modified = time.strftime("%m/%d/%Y %I:%M:%S %p",
            time.localtime(os.path.getmtime(path)))
        return modified
    
    def ctime(self, path):
        """Gets creation time"""

        created = time.strftime("%m/%d/%Y %I:%M:%S %p",
            time.localtime(os.path.getctime(path)))
        return created

    def atime(self):
        """Gets current time"""
        
        access_time = time.strftime("%m/%d/%Y %I:%M:%S %p")
        return access_time         


class Walk(FileAttrHelper):
    
    """Generator Based Walk API that yield populated File Objects"""

    def __init__(self, path = None):
        self.path = path
        self.fileob = FileOb()

    def mkfileob(self, mkhash = False):
        """Yields a populated FileOb instance"""
        
        fileob = self.fileob 
        for root, directory, files in os.walk(self.path): 
            for file in files:
                fileob.name = file
                fileob.abspath = os.path.abspath(os.path.join(root, file)) 
                fileob.ext = self.extension(file)
                if mkhash:
                    fileob.hash = self.checksum(fileob.abspath)
                fileob.modified = self.mtime(fileob.abspath) 
                fileob.created = self.ctime(fileob.abspath)
                fileob.accessed = self.atime()
                fileob.symbolic = os.path.islink(fileob.abspath) 
                fileob.size = os.path.getsize(fileob.abspath)
                yield fileob
