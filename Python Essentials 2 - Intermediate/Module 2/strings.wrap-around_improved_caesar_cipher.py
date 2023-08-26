'''                                          2.5.1.6 LAB: Improving the Caesar cipher

DIFFICULTY: Hard

OBJECTIVES:
-Enhance the Caesar cipher from the previous lab which shifted by only one character. Allow shifts in the range of 1..25.
-Preserve letter casing and leave non-alphabetical characters untouched.
-Prompt the user for text input to encrypt.
-Obtain a shift value from the user.
-Display the encoded text.

TEST DATA 1                                                         TEST DATA 2
=========                                                           ==========

Sample input:       Sample output:                                  Sample input:      Sample output:

abcxyzABCxyz 123    cdezabCDEzab 123                                The die is cast    Sgd chd hr bzrs
2                                                                   25


REFERENCES:
"The modulo (%) for wrap-around iteration is the only part where I referred to notes."
'''




sentence = input("Please enter a line of text to encrypt: ")
shift_value = int(input("Please enter a shift value from 1 to 25: "))
alphabet = ''
looped_alphabet = ''
cipher_sentence = ''

for i in range(65, 90 + 1):  # create string containing full uppercase alphabet A - Z using ASCII numbers
    alphabet += chr(i)

for c in sentence: # loop through user's text one character at a time

    if c.isalpha() == False: # don't process non-alphabetical characters (just copy to new cipher)
        cipher_sentence += c
    else:
        idx = alphabet.find(c.upper()) # get index of character in alphabet (remember the alphabet is uppercase)
        
        for i in range(shift_value + 1): # repeat 'shift_value' times
            looped_alphabet += alphabet[(i + idx) % len(alphabet)] # build new alphabet (one character at a time) starting from the index of the current character (c);  NOTE: modulo ensures wrap around (simpler example in comments below)
        cipher_character = looped_alphabet[-1]
        
        if c.islower():
            cipher_character = cipher_character.lower()
        
        cipher_sentence += cipher_character
print("New encrypted line of text (Cipher) is: ", cipher_sentence)














'''                                                   MODULO WRAP-AROUND 
text = "example"
length = len(text)
num_iterations = 10  # Adjust this value as needed

for i in range(num_iterations):
    char = text[i % length]
    print(char)
'''














'''
DISCUSSION BOARD POST (copy for reference later)

This lab was challenging. Still, I managed to get a perfect result using the sample test data provided and without viewing the hint or solution.

The lab discussed ASCII conversions. I used ASCII for characters to avoid manual alphabet entry, but didn't need to convert back. Thus, I still wanted to check the official solution (hint):

Official Solution:
By subtracting 65 (ascii for 'A') from the shifted ascii, calculating its remainder when divided by 26, and then adding 65 back, the desired result is achieved. But honestly, how was I supposed to arrive at this specific method? My approach was lengthier, focusing on logical flow (I devised a 'more verbose' method to wrap-around my loop through the alphabet) rather than using a precise mathematical shortcut which wasn't inherently obvious.

While I see the merit in pre-coding numeric exploration, the formula's intricacy implies a need for clearer guidance. The hint's code is direct; its unique formula trims verbosity.
From this lab, I've learned:

A) Modulo (%) enables wrap-around iteration.
B) Before coding, invest time in deducing formulas.

The official solution/hint is below:
'''




'''
# input text to encrypt
text = input("Enter message: ")

# enter valid shift value (repeat until it succeeds)
shift = 0

while shift == 0:
    try:    
        shift = int(input("Enter cipher's shift (1..25): "))
        if shift not in range(1,26):
        	raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print("Bad shift value!")

cipher = ''

for char in text:
    # is it a letter?
    if char.isalpha():
        # shift its code
        code = ord(char) + shift
        # find the code of the first letter (upper- or lower-case)
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        # make correction
        code -= first         # code 35
        code %= 26
        # append encoded character to message
        cipher += chr(first + code)
    else:
        # append original character to message
        cipher += char

print(cipher)
'''