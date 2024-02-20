# type: ignore # pylint: disable=all
"""                                               STRING METHODS                                               """
# NOTE: ALL string methods return something.

str.capitalize() # Return a copy of the string with ONLY its first character capitalised and THE REST LOWERCASED.
str.title() # makes the first letter in each word upper-case.
str.upper() # converts all the string's letters into upper-case letters.
str.lower() # converts all the string's letters into lower-case letters.
str.swapcase() # swaps the letters' cases.

str.center(width[, fillchar]) # centers the string inside the field of a known length;                                                               

# NOTE: String Methods with Slices: 'start' can be used without 'end' but 'end' cannot be used without 'start'.
str.count(sub[, start[, end]]) # counts the occurrences of a given character;
str.find(sub[, start[, end]]) # finds a substring returning its index, or -1 on failure; (start inclusive, end exclusive);    string.find('text', start, end)
str.rfind(sub[, start[, end]]) # Return the HIGHEST INDEX where the START of the substring is found (from left to right). Returns -1 if failed; (start inclusive, end exclusive);
str.index(sub[, start[, end]]) # Like find(), but raise ValueError when the substring is not found.

str.join(iterable)# joins all items of a tuple/list into one string (the invoked string acts as item seperator);
str.split(sep=None, maxsplit=- 1) # splits the string into a substring list using a given seperator. 'maxsplit' refers to the max number of break points, not peices or elements.

str.strip([chars]) # removes the leading and trailing white spaces (or specified adjacent characters);
str.lstrip([chars]) # removes the white characters from the beginning of the string (or specified adjacent characters);
str.rstrip([chars]) # removes the trailing white spaces from the end of the string (or specified adjacent characters);

str.replace(old, new[, count]) # replaces a given substring with another.  THE THIRD ARG IS HOW MANY INSTANCES (FROM THE LEFT) TO REPLACE;



"""                                       BOOLEAN STRING METHODS                                               """

str.startswith(prefix[, start[, end]]) # does the string begin with a given substring?
str.endswith(suffix[, start[, end]]) # does the string end with a given substring?

str.isupper() # does the string consists only of upper-case letters?
str.islower() # does the string consists only of lower-case letters?

str.isalnum() # does the string consist only of letters and digits?
str.isalpha() # does the string consist only of letters?

str.isnumeric() # Covers digits, numeric characters from other languages, and special numeric characters (like Roman numerals and fractions).
str.isdigit() #  Includes decimals, standard digits and special digit characters (like superscripted and subscripted digits). 
str.isdecimal() # Only standard decimal characters used in base 10 number systems, excluding numerals from other languages and special numeric characters.

str.isspace() # does the string consists only of white spaces? Space (' ')    Tab ('\t')     Newline ('\n')     Return ('\r')     Formfeed ('\f')     Vertical Tab ('\v')





# ASCII BOOLEAN CHECKER
print('ASCII   Character   Types')
for i in range(ord(chr(32)), ord(chr(128))):
    print(i, chr(i), 'isalnum()' if chr(i).isalnum() == True else '',  'isalpha()' if chr(i).isalpha() == True else '',  'isdigit()' if chr(i).isdigit() == True else '',  'isdecimal()' if chr(i).isdecimal() == True else '',  'isnumeric()' if chr(i).isnumeric() == True else '', 'isspace()' if chr(i).isspace() == True else '', sep="         ")

