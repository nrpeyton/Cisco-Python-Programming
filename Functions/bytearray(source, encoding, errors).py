bytearray(source, encoding, errors) # Creates a new array of bytes from the source. Returns a bytearray object.

'''
source: The source to initialise the array of bytes. Could be a string, an integer, a bytes object, or an iterable.
encoding: Required if the source is a string. The encoding of the string.
errors: Specifies the action to take if the decoding fails. Default is 'strict'.
Examples:
'''

# Create an empty bytearray
empty_byte_array = bytearray()  # bytearray(b'')


# Create bytearray from string with encoding
string_byte_array = bytearray("Hello", 'utf-8')  # bytearray(b'Hello')
# OR
# Create bytearray from bytes
bytes_byte_array = bytearray(b'Hello')  # bytearray(b'Hello')


# Create bytearray from list of integers
list_byte_array = bytearray([65, 66, 67])  # bytearray(b'ABC')

# Create bytearray of a certain size filled with zero bytes
zero_byte_array = bytearray(5)  # bytearray(b'\x00\x00\x00\x00\x00')

# Create bytearray from file
try:
    stream = open("image.png", "rb")
    image = bytearray(stream.read())
    stream.close()
except IOError:
    print("failed")
else:
    print("success")

# Used for mutable binary data manipulation and I/O operations.
