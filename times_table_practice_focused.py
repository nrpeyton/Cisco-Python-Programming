from random import randint, choice
from sys import exit

times_table = 0
times_tab_set = set()


def get_times_table():
    tt = int(input("""
    Practice Mode: Enter 'times table' to practice (i.e,. 3 to 12)
    Focus Mode: Enter -1
    Exit: Enter -2
    > """))
    return tt


def process_set(is_correct, times_table, operand):

    if is_correct == False and (times_table, operand) not in times_tab_set:
        times_tab_set.add((times_table, operand))


def challenge_user(times_table, operand):
    user_answer = int(input(f'What is {operand} * {times_table}?: ')) if choice([1, 2]) == 1 else int(input(f'What is {times_table} * {operand}?: '))
    is_correct = True if times_table * operand == user_answer else False
    
    print('Correct') if is_correct else print(f'Incorrect (added to Focus list): the correct answer is {times_table * operand}')
    process_set(is_correct, times_table, operand)



while times_table != -2:
    times_table = get_times_table()

    if times_table != -1 and times_table != -2:
        for o in range(15):
            operand = randint(3, 12)
            challenge_user(times_table, operand)

    elif times_table == -1:
        if len(times_tab_set) > 2:
            for i in range(15):
                tup = choice(list(times_tab_set))
                challenge_user(tup[0], tup[1])
        else:
            print("Minimum 3 (unique) incorrect answers required before using Focus Mode.  Switching back to main menu...")
            times_table = 0

    else:
        exit()