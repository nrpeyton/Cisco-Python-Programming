# from random import randint, choice

# min, max = 0, 3
# lst = [chr(randint(ord('a'), ord('z'))) + chr(randint(ord('a'), ord('z'))) + chr(randint(ord('a'), ord('z'))) for i in range(min, max)]
# lst.sort() # sorts in-place
# print(lst)
# lst = list(enumerate(lst))
# print(lst)

# str_to_find = choice(lst)[1]
# print('String to find:', str_to_find)

# guess = None
# while guess != str_to_find:
#     midpoint = (min + max) // 2
#     guess = lst[midpoint][1]
#     print('Guess:', guess)
#     if guess == str_to_find:
#         print('String Found')
#         break
#     elif guess > str_to_find:
#         max = midpoint
#         print('changed max to:', max)
#     elif guess < str_to_find:
#         min = midpoint + 1
#         print('changed min to:', min)
    



# Official (slightly) more elegant version from Khan Academy with primes
def do_search(array, target_value):
    min = 0
    max = len(array) - 1
    guess = None
    while max >= min:
        guess = (max + min) // 2
        if array[guess] == target_value:
            return guess
            
        elif array[guess] < target_value:
            min = guess + 1
            
        else:
            max = guess - 1
            
    return -1


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
target_value = 19

result = do_search(primes, target_value)
print(result)