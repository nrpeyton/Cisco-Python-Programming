'''                                             4.3.1.15 LAB: Character Frequency Histogram

DIFFICULTY: Medium
TIME: 30-60 minutes

OBJECTIVES:
-Enhance file handling capabilities, specifically reading from files.
-Utilize data collections for efficient data counting.

SCENARIO:
Analyze the frequency of each Latin alphabet letter in a text file for cryptographic analysis.

FEATURES:
-Prompt user for the name of the input file.
-Read the file and count the frequency of each Latin letter, disregarding case.
-Display a histogram of the letter frequencies in alphabetical order; show only non-zero counts.

TEST DATA:
Sample Input File Content: aBc
Expected Output:
a -> 1
b -> 1
c -> 1

TIPS:
-Use a dictionary for storing counts. Letters are keys; frequencies are values.
'''

from os import strerror

def get_filename(fn):
    if len(fn) < 1: # Only prompt for input if the string argument in the call to get_filename() is empty.
        fn = input("Enter file name: ")
    return fn

filename = get_filename('text_file_char_freq_histog.txt') # Add filename here or leave empty to have the program prompt for input.

try:
    stream = open(filename, 'rt')
except IOError as e:
    print("Can't open file: ", strerror(e.errno))

data = stream.read() # Read all text and assign to data.
stream.close()
data = data.lower() # Convert all text data to lowercase.

dict = {}
for i in range(ord('a'), ord('z') + 1):
    ct = data.count(chr(i)) # Counts the number of each letter a to z.
    dict[chr(i)] = ct # Adding an item to the dictionary is done by specifying a new index key and assigning a value to it.
    
    if dict[chr(i)] > 0: # Only print the dictionary key's value if the current letter is present in the source file.
        print(chr(i), '->', dict[chr(i)])









'''                                             4.3.1.16 LAB: Improved Character Frequency Histogram

DIFFICULTY: Medium
TIME: 15-30 minutes
PREREQUISITES: 4.3.1.15

OBJECTIVES:
-Advance file handling skills, encompassing both reading and writing.
-Master the use of lambdas for custom sorting.

SCENARIO:
Optimize the previous lab's code to enhance the histogram's output and storage.

FEATURES:
-Sort the histogram based on character frequency, higher counts first.
-Output the histogram to a file with the same name as the input, appending '.hist' to the name.

TEST DATA:
Sample Input File Content: cBabAa
Expected Output File Content:
a -> 3
b -> 2
c -> 1

'''


sorted_list = sorted(dict.items(), key=lambda elem: elem[1], reverse=True) # The 'key' parameter in the 'sorted' function automatically passes each tuple (element) to the lambda function for sorting.  An alternative style is shown below***.
print(sorted_list) # temp

filtered_list = list(filter(lambda elem: elem[1] > 0, sorted_list)) # Filter out tuples with zero letter frequency counts.
print(filtered_list) # temp

try:
    stream_dest = open(filename + '.hist', 'wt')
    
    for t in filtered_list:
        stream_dest.write(t[0] + ' -> ' + str(t[1]) + '\n') # Write in expected test data format.

    stream_dest.close()

except IOError as e:
    print("Can't write file: ", strerror(e.errno))




''' ***
def take_second(elem):
    return elem[1]

srtd_dict = sorted(dict.items(), key=take_second, reverse=True)    # alternative style for dictionary sort.
'''