Pathtool creates an very efficient API to the filesystem paths.  Usage is dirt simple.  You only need to call the path function with a fullpath, an optional pattern, and an optional action callback.


**Pathtool**:  An efficient Python Path API


Author: Noah Gift
Version: $Revision: 0.1.1 $
Copyright: This document has been placed in the public domain.

# Summary #

You can find a practical example of how to use this API here:

https://www.ibm.com/developerworks/aix/library/au-cli_plugins/

Pathtool is an efficient API to walking a filesystem, and it aims to be
very simple, yet powerful.  By calling path you can pass it a path to a
filesystem, apply an optional unix style pattern filter, and an optional
action callback function.

This allow you to powerful things to a filesystem in one line of code.  You
search a directory

There is a record dictionary that contains useful key/value combinations such
as a unique\_id hash, ctime, mtime, size, and extension.  These records can easily
be used to create custom action callbacks.  Additionally a future API will integrate
chainable actions.

Update:  A commandline tool example has been created along with a simple plugin
architecture.  You can see that here:

http://code.google.com/p/pathtool/source/browse/trunk/cli/pathtool_cli.py

# Example Library Usage #

from pathtool import path

path("/tmp", pattern=".mp3")

This would search the /tmp directory and return the path to all matches to the `*.mp3`
pattern.  This is because it is using a default callback action that just prints out
the path to a match.  You can create your own callback and do things like create tar
archives, delete files, move files, deduplicate files, compare sizes, etc.

The API is subject to some small changes, so no promises for now.

# Example CLI Usage #


Coming soon...
QUESTIONS:  noah dot gift at gmail.com

---
