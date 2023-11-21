from os import uname # <--- For Unix.  For windows, use `from platform import uname`

print(uname())

''' 
OUTPUT:
nodename — stores the machine name on the network;
release — stores the operating system release;
version — stores the operating system version;
machine — stores the hardware identifier, e.g., x86_64.
'''





from os import name

print(name)

'''
OUTPUT:
posix — you'll get this name if you use Unix;
nt — you'll get this name if you use Windows;
java — you'll get this name if your code is written in Jython.
'''





import os

os.listdir() # same as Unix `ls` command
os.chdir() # same as `cd`
os.getcwd() # get current working directory (same as Unix `pwd`)

os.mkdir() # same as Windows and Unix `mkdir` command
os.rmdir()

os.makedirs() # recursive (similar to `mkdir -p` in Unix)
os.removedirs()

os.system("command") # allows any regular OS shell command. In Unix an 'exit status 0' is returned indicating sucess.  In Windows; the shell response is returned.  DOES NOT MAINTAIN STATE BETWEEN CALLS (i.e., don't use with "cd" to pre-empt another line's command).