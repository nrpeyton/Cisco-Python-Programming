def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[0][0],"   |   ",board[0][1],"   |   ",board[0][2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[1][0],"   |   ",board[1][1],"   |   ",board[1][2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")
    print("|       |       |       |")
    print("|   ",board[2][0],"   |   ",board[2][1],"   |   ",board[2][2],"   |", sep='')
    print("|       |       |       |")
    print("+-------+-------+-------+")


def enter_move(board, free_fields):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    player_move = int(input("Enter your move: "))

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == player_move:
                move_coordinates = (row, column)
                if move_coordinates in free_fields:
                    board[row][column] = 'O'
    return board


def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_fields = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != 'O' and board[row][column] != 'X':
                free_fields.append((row, column))
    print("free fields", free_fields)
    return free_fields


def victory_for(board):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for row in range(len(board)):
        if ['X', 'X', 'X'] == board[row]:
            print("Horizontal Match Found")
            sign = 1 # computer wins
            return sign
        elif ['O', 'O', 'O'] == board[row]:
            print("Horizontal Match Found")
            sign = 2 # player wins
            return sign
        else:
            for column in range(3):
                if board[0][column] == 'X' and board[0 + 1][column] == 'X' and board[0 + 2][column] == 'X':
                    print("Vertical Match Found")
                    sign = 1 # computer wins
                    return sign
                elif board[0][column] == 'O' and board[0 + 1][column] == 'O' and board[0 + 2][column] == 'O':
                    print("Vertical Match Found")
                    sign = 2 # player wins
                    return sign
                elif board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
                    print("Diagonal Match Found")
                    sign = 1 # computer wins
                    return sign
                elif board[2][0] == 'X' and board[1][1] == 'X' and board[0][2] == 'X':
                    print("Diagonal Match Found")
                    sign = 1 # computer wins
                else:
                    return 0 # continue game


def draw_move(board, free_fields):
    # The function draws the computer's move and updates the board.
    from random import randrange
    computer_move = randrange(1,10)

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == computer_move:
                move_coordinates = (row, column)
                if move_coordinates in free_fields: # check if field is free
                    board[row][column] = 'X'
                else:
                    draw_move(board, free_fields)
    return board


board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
sign = 0 # continue (0), computer win (1), player win (2)
free_fields = make_list_of_free_fields(board)

while sign == 0 and len(free_fields) > 0:
    display_board(board)
    sign = victory_for(board)
    free_fields = make_list_of_free_fields(board)
    board = enter_move(board, free_fields)
    display_board(board)
    sign = victory_for(board)
    free_fields = make_list_of_free_fields(board)
    board = draw_move(board, free_fields)
if sign == 1:
    print("You lost!")
elif sign == 2:
    print("You won!")
else:
    print("The game tied.")