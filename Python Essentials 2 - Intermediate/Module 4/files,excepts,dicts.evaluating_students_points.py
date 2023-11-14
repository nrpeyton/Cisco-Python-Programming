from os import strerror
import sys


class StudentsDataException(Exception):
    pass


class BadLine(StudentsDataException):
    pass


class FileEmpty(StudentsDataException):
    pass

# Function to check the validity of each line in the file
def line_checker(l):
    '''
    Validate each line to ensure:
    - Minimum length of 7 characters
    - Contains exactly two 'tab' characters as delimiters
    - The last character is not alphabetic
    '''
    if len(l) < 7:
        raise BadLine("Bad line")
    elif l.count(chr(9)) < 2:
        raise BadLine("Bad line")
    elif l[-1].isalpha() != False:
        raise BadLine("Bad line")
    else:
        return "okay"

# Function to read a line from the file    
def line_reader(fn):
    try:
        l = stream.readline()
        return l
    except IOError as e:
        sys.exit(e)

dct = {} # Initialize an empty dictionary to store student data
file_name = input("Please enter the file name: ") # User input for file name

# Open the file and handle possible IO errors
try:
    stream = open(file_name, 'rt')
    line = line_reader(file_name) # Read the first line.
except IOError as e:
    sys.exit(e)

try:
    if len(line) < 1:
        raise FileEmpty("File empty")

# Main logic to process file and populate student data dictionary   
    while len(line) > 0: # Continue until end of file
        if line_checker(line) == "okay":
            lnlst = line.split(chr(9)) # Split line into a list (3 columns) using 'tab' as a delimiter
            if len(lnlst) != 3: # Check for three columns (i.e., an element for name, surname and points)
                raise BadLine("Bad line")
            name = lnlst[0] + ' ' + lnlst[1] # Form the full name and get points:
            points = float(lnlst[2]) # Convert points to float

# Populate dictionary with student data  
        if name not in dct:
            dct.update({name: points})
        elif name in dct: # Handle multiple entries for the same student
            points += float(dct[name])
            dct.update({name: points})
        
        line = line_reader(file_name)

except BadLine as e:
    sys.exit(e)
except FileEmpty as e:
    sys.exit(e)
except StudentsDataException as e:
    sys.exit(e)
    
try:
    stream.close()
except IOError as e:
    sys.exit(e)

# Print sorted student data
for x, y in sorted(dct.items()):
    print(x + chr(9) + str(y))





'''     Post-completion reflections:

In hindsight when reading from the file; I would open() the stream, perform stream.readlines() on the whole file, then close(), instead of risking an IO error with every fetched line:

stream.readlines() creates a list; one element per entire line.  IOError could then be included in the main try-except block, instead of being separated.

'''