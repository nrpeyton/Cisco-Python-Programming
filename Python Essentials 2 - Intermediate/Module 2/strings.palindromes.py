'''                                             2.5.1.7 LAB: Palindromes

DIFFICULTY: Easy

OBJECTIVES:
- Enhance string manipulation skills.
- Encourage non-obvious solution-seeking.

SCENARIO:
Check if the user-input text is a palindrome, considering:
- Ignoring letter casing.
- Excluding spaces.

TEST DATA 1                                                     TEST DATA 2
===========                                                     ===========

Sample input:                   Sample output:                  Sample input:                      Sample output:

Ten animals I slam in a net     True                            Eleven animals I slam in a net     False
'''




word = ''
n = -1
result_recorder = ''

sentence = input("Palindrome (true/false) checker:  Enter the sentence to be checked: ").lower()     # make lower case
for c in sentence:
    word += c.lstrip()     # remove white spaces

for i in range(len(word)):
    for c in word[i]:     # for each char starting with word[0]
        if c == word[n]:     # check if its equal to last letter, second last letter, third last letter, -4, -5, etc., ...
            result = True
            result_recorder += 'T'     # record comparison result
        else:
            result = False
            result_recorder += 'F'     # record comparison result
        n -= 1     # reduce index, -1, -2, -3, etc., ...

print(result_recorder.count('F') == 0)     # print result





''' Personal Notes:
Nieve method here.  Less verbose method below:
'''









word = ''
result = True

sentence = input("Palindrome (true/false) checker:  Enter the sentence to be checked: ").lower()     # make lower case
for c in sentence:
    word += c.lstrip()     # remove white spaces

for i in range(len(word)):
    if word[i].startswith(word[-i -1]): # string method checks word's beginning index against its end index, then second vs second last, third vs third last, etc., ...
        result = True
    else:
        result = False
        break
print(result)




''' Personal Notes:
Cleaner (less verbose) method.  Course materials not used, but did refer to docs.python.org for string .startswith() method syntax.
'''