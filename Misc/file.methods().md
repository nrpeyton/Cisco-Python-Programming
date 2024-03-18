#                               T E X T    M E T H O D S   (class io.TextIOBase)

"""REMEMBER: The mode used with the built-in function open() determines the class of the file object. [See open() function](../Functions/open().md) """

#                                                 WRITING (w, a, r+, w+, a+)
file.write(string) # Takes a string and appends it at the current file position.  Returns the number of bytes/characters written.

file.writelines(lines, /)  # Write a list of lines at the current file position. Newline separators ('\n') are not added.

#                                                 READING (r, r+, w+, a+)
file.read([size= -1], /)  # Reads entire file or number of characters/bytes from current position, returning empty string at EOF.

file.readline([size = -1], /)  # Returns the next line from the file up to the newline character or size of byteas, whichever is first. 
                              #If EOF, returns an empty string.

file.readlines(hint = -1, /): # Returns the next list of lines from the file. If 'hint' bytes (approximate) are read, no further lines are read.
                             # An empty list is returned if EOF.


#                                 B I N A R Y   M E T H O D S   (class io.BufferedIOBase)

#                                                 WRITING (wb, ab, r+b, w+b, a+b)
file.write(bytearray): # Writes the contents of 'bytearray' to the current file position. Returns the number of bytes written.

#                                                 READING (rb, r+b, w+b, a+b)
file.read([size]): # Reads the entire file or up to 'number' bytes if specified. Returns a bytes object.

file.readinto(bytearray): # Reads bytes from the file into 'bytearray'. Returns the number of bytes read.


# Example: 
bytearray_variable = bytearray(100)
file.readinto(bytearray_variable)

MUTABILITY:
Bytearray objects are mutable and can be modified.
Bytes objects are immutable.

"""REMEMBER: Use file.close() or a 'with' statement for automatic closing and saving. 

For advanced usage and error handling, refer to the [Python File I/O Documentation](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files)."""
