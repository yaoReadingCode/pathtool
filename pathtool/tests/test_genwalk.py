import unittest
import doctest

try:
    from pathtool import genwalk
except ImportError:
    import sys
    sys.path.append("/Users/ngift/src/pathtool/branches/v2_file_dir_objects/")
    from pathtool import genwalk

class TestFileOb(unittest.TestCase):
    
    def setUp(self):
        pass

    def test_init(self):
        """Test General Package Import.  
        
        This just ensures package is in path, so tests work"""
        
        try:
            genwalk.FileOb()
        except:
            self.fail()

if __name__ == "__main__":
    unittest.main() 
