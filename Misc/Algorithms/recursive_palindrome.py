def first_character(str):
    """Returns the first character of the string str."""
    return str[0:1]

def last_character(str):
    """Returns the last character of a string str."""
    return str[-1:]

def middle_characters(str):
    """Returns the string that results from removing the first
    and last characters from str."""
    return str[1:-1]

def is_palindrome(str):
    """Determines if a string is a palindrome."""
    
    # base case #1
    if len(str) == 0 or len(str) == 1:
        return True

   # base case #2
    if first_character(str) != last_character(str):
        return False
    
    #recursive case
    else:
        return is_palindrome(middle_characters(str))


def check_palindrome(str):
    """Prints whether a word is a palindrome."""
    print(f"\nIs this word a palindrome? {str}")
    print(is_palindrome(str))

# Testing the base case
check_palindrome("a")
# Uncomment the following line once you implement base case #2 and recursive case
assert is_palindrome("a") == True

check_palindrome("motor")
# Uncomment the following line once you implement base case #2 and recursive case
assert is_palindrome("motor") == False

check_palindrome("rotor")
# Uncomment the following line once you implement base case #2 and recursive case
assert is_palindrome("rotor") == True

check_palindrome("cool")
# Uncomment the following line once you implement base case #2 and recursive case
assert is_palindrome("cool") == False

check_palindrome("racecar")
# Uncomment the following line once you implement base case #2 and recursive case
assert is_palindrome("racecar") == True

check_palindrome("tattarrattat")
# Uncomment the following line once you implement base case #2 and recursive case
assert is_palindrome("tattarrattat") == True
