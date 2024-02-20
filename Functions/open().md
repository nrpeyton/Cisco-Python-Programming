fileObject.open(./'text.txt', 'r' )

Read Mode (`r`): Opens the file for reading from the beginning. Raises errno.ENOENT if the file doesn't exist.

Write Mode (`w`): Opens and truncates the file to zero length or creates a new one, starting at the beginning.

Append Mode (`a`): Opens the file for appending at the end or creates a new one.

Exclusive Creation (`x`): Creates a new file FOR WRITING, raises errno.EEXIST if it exists.

Read and Write (`r+`): Opens the file for both reading and writing from the beginning. Raises errno.ENOENT if the file doesn't exist.

Write and Read (`w+`): Opens the file for both reading and writing, truncating or creating it as needed, starting at the beginning.

Append and Read (`a+`): Opens or creates the file for both reading and appending at the end.  Writes always move the file position (back) to the end.

+
beside write, '+''  means read; 
beside read, '+'' means write (aka update)

# Crucial difference between w+ and r+, is with r+ the file must already exist.




APPEND & READ (`a+`)

                                        # file.txt exists and was created using the next three lines:
# f = open('file.txt', 'w+')
# f.write('line 1\nline 2\nline 3\nline 4')
# f.close()

f = open('file.txt', 'a+')
f.seek(0)
s1 = f.read() + '    ...first read'      # reads succesfully
f.write('new line')                      # ignores seek() and (successfully) appends the string at the end
s2 = f.read() + '    ...second read'     # nothing is read, because the 'a' mode "forced" write() to moved the head to the end before writing
f.close()
print(s1)
print(s2)

# Always remember to re-position the head using seek() after a write operation in 'append & read' (a+) mode.