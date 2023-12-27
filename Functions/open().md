fileObject.open(./'text.txt', 'r' )

Read Mode (`r`): Opens the file for reading from the beginning. Raises errno.ENOENT if the file doesn't exist.

Write Mode (`w`): Opens and truncates the file to zero length or creates a new one, starting at the beginning.

Append Mode (`a`): Opens the file for appending at the end or creates a new one, starting at the beginning.

Exclusive Creation (`x`): Creates a new file for writing, raises errno.EEXIST if it exists.

Read and Write (`r+`): Opens the file for both reading and writing from the beginning. Raises errno.ENOENT if the file doesn't exist.

Write and Read (`w+`): Opens the file for both reading and writing, truncating or creating it as needed, starting at the beginning.

Append and Read (`a+`): Opens the file for both reading and appending at the end. Only 'reads' honour seek() changes, i.e., 'appends' only at the end.

Crucial difference between w+ and r+, is with r+ the file must already exist.