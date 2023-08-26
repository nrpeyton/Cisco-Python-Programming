'''                                         2.5.1.8 LAB: Anagrams


DIFFICULTY: Easy

OBJECTIVES:
- Enhance string manipulation skills.
- Convert between strings and lists.

SCENARIO:
Determine if two user-input texts are anagrams, considering:
- Ignoring letter casing.
- Excluding spaces.

TEST DATA 1                                                       TEST DATA 2
=========                                                         ==========

Sample input:       Sample output:                                Sample input:      Sample output:

Listen              Anagram: True                                 modern             Anagram: False 
Silent                                                            norman

'''





text1 = input("Enter first text: ").lower()
text1 = text1.replace(' ', '')
text1 = sorted(list(text1))

text2 = input("Enter second text: ").lower()
text2 = text2.replace(' ', '')
text2 = sorted(list(text2))

for i in range(len(text1)):
    if text1[i] == text2[i]:
        anagram = True
    else:
        anagram = False
        break

print("Anagram: ", anagram)