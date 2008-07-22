"""My callback plugin that moves matches to the tmp directory"""
import shutil

def plugin(rec, verbose=True):
    """Moves matched files to tmp directory"""
    path = rec["path"]
    tmp_path  = "/tmp/%s" % rec["filename"]
    if verbose:
        print "Moving %s to %s" % (path,tmp_path)
    shutil.move(path, tmp_path)
