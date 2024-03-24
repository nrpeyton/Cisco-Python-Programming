#                                              FINAL ASSESSMENT - PRACTICAL ACTIVITY: Cipher Generator
# Nicholas Peyton
# J9581959_TZFM163_30
    

class Encryption:
    """
    This class provides a Caesar based cipher generator.
    """

    def __init__(self) -> None:
        """"
        Initialises the class with a default shift value of 0; aids graceful exit on KeyboardInterrupt.
        """
        self.__shift_value: int = 0
        self.__word: str = ''

    def get_user_input(self) -> None:
        """"
        This method asks the user for the word or text to be encrypted, and for their birth month which acts as a key.
        Input validation is performed; and, provides option to exit gracefully without mandatory input.
        """

        self.__word = input("Please enter word(s) or text to be encrypted: ")
        
        while True: # Loop continues until input is valid or user exits gracefully.
            try:
                bday_m = int(input("Please enter your birth month (01 to 12): ")) 
                if bday_m >= 1 and bday_m <= 12: # Validate input 'before' updating self.__shift_value to guard against invalid or unwanted encryption on KeyboardInterrupt.
                    self.__shift_value = bday_m
                    break
            except KeyboardInterrupt: # Enables user to exit without mandatory input.
                print("Program ended gracefully: Word was not encrypted:")
                break
            except:
                print("Invalid Input - Please only enter a valid birthday month (1 to 12):") # Repeats until valid, or KeyboardInterrupt.

    def encrypt(self) -> str:
        """
        Encrypts the user's word/text based on the Caesar algorithm and returns the cipher.
        Non-alphabetical characters are simply copied to the new cipher string, preserving original position.
        Modulus based formula allows wrapping back around to 'A' after 'Z'.
        """
        cipher: str = '' # Initialise cipher string.
        ascii_uppercase_start = ord('A') # ASCII code for start of uppercase alphabet, used in Modulus formula below.
        ascii_lowercase_start = ord('a') # '' ''                   lowercase                                    '' ''
        
        for c in self.__word: # Loop through user's word or text.
            ascii_letter = ord(c) # Get current character's ASCII code.

            if c.isalpha() == False: # If a character in the user's word/text is not a letter, do not encrypt it; only copy it:
                cipher += c
            elif c.isupper():
                cipher += chr((ascii_letter + self.__shift_value - ascii_uppercase_start) % 26 + ascii_uppercase_start) # After Z, formula allows wrapping back around to A (Padhye et al., 2018).
            elif c.islower():
                cipher += chr((ascii_letter + self.__shift_value - ascii_lowercase_start) % 26 + ascii_lowercase_start) # '' ''
        
        return cipher

if __name__ == "__main__": # Prevents implicit execution on import (Padhye et al., 2018).
    cipher_generator = Encryption() # Create encryption object
    cipher_generator.get_user_input() # Get cipher's user defined paramaters
    print("Cipher:", cipher_generator.encrypt()) # Print encrypted output.
