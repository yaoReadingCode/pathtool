In order to write a plugin, you only need
to write a file that conforms correctly to the action
callback spec, and name your file as follows:

mycallback.plugin

The callback spec is as follows.  It could be helpful to look at the
existing callback to find out more:

action = (lamda rec: print_rec(rec))

rec = {"path": path, "filename": file, "ext": ext, "size": size,
                "unique_id": unique_id, "mtime": mtime, "ctime": ctime}


New callback:

action=(lambda rec: print_rec(rec))



