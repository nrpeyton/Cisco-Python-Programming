# TERMINAL/COMMAND PROMPT ARGUMENTS (i.e., flags)

print('hello')

import sys
print(sys.argv)

"""
SCRIPT
Running as a script only outputs a single element list containing this file's path.

COMMAND LINE
Output when this file is run from a terminal, i.e., `python3 argv.py hi hello test` is:
['argv.py', 'hi', 'hello', 'test']
"""