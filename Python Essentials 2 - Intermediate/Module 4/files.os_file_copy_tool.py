# Tool similar to Windows DOS 'copy' command or Linux 'CP' command.

from os import strerror

srcname = input("Enter the source file name: ")
try:
    src = open(srcname, 'rb') # Specify source filename; create a stream object.
except IOError as e:
    print("Cannot open the source file: ", strerror(e.errno))
    exit(e.errno) # Forces the interpreter to quit the entire program; nothing further is interpreted.

dstname = input("Enter the destination file name: ") # Specify destination file name (for new copied file).
try:
    dst = open(dstname, 'wb') # Specify destination filename; create a stream object.
except Exception as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    src.close()
    exit(e.errno)	

buffer = bytearray(65536) # Create an object of the bytearray class.
total  = 0 # Initialise counter.
try:
    readin = src.readinto(buffer) # The stream.readinto() method reads the stream, transferring INTO (and filling) the data structure in its argument: the buffer, not the destination file (yet).  It also returns the number of bytes read (hence readin = ...).
    while readin > 0: # Remember everytime stream.readinto() or stream.read() is used on an open (non-closed) stream, the file pointer/cursor (or "virtual read/write head") moves to the end of the number of bytes read.  If/when it reaches the end of the file/stream, source.readinto() will eventually return '0' for number of bytes read.
        written = dst.write(buffer[:readin]) # Write the buffer to the stream object.  The stream.write() method also returns the number of bytes written.  A slice is used because the last read almost certainly won't fill the entire buffer.
        total += written
        readin = src.readinto(buffer) # Fill the buffer with the next 64kb, and continue the while loop until reaching the end of the file/stream.
except IOError as e:
    print("Cannot create the destination file: ", strerror(e.errno))
    exit(e.errno)	

print(total,'byte(s) succesfully written')
src.close()
dst.close()
