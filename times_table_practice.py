from random import randint, choice

times_table = int(input("Which times table to practice?: "))
for o in range(3, 50):
    mult = randint(3, 12)
    user_answer = int(input(f'What is {mult} * {times_table}?: ')) if choice([1, 2]) == 1 else int(input(f'What is {times_table} * {mult}?: '))
    is_correct = True if times_table * mult == user_answer else False
    print('Correct') if is_correct else print(f'Incorrect: the correct answer is {times_table * mult}')
