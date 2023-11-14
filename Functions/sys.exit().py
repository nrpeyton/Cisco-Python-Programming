'''
sys.exit([arg])

Description:
The exit() function from the sys module exits Python by raising the SystemExit exception. 'arg' specifies an exit status (default is 0 for success, non-zero for error). 
It's ideal to prevent your module's user from running module code as an ordinary/standalone script, and less so for larger, complex applications that require 
more graceful exits.  It is handled as a normal exception in try-except and finally blocks.


Example:
'''

import sys

if __name__ == "__main__":
    print("Don't do that!")
    sys.exit()


# Note: The use of sys.exit() should be considered in the context of the entire application, as it exits the Python interpreter and may interrupt ongoing processes or threads.
