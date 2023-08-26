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


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    player_move = int(input("Enter your move: "))

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == player_move:
                move_coordinates = (row, column)
                if make_list_of_free_fields(board, move_coordinates) == True: # check if field is free
                    board[row][column] = 'O'
    return board


def make_list_of_free_fields(board, move_coordinates):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

    free_squares = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] != 'O' and board[row][column] != 'X':
                free_squares.append((row, column))
    print("free squares", free_squares)

    if move_coordinates in free_squares:
        return True
    else:
        return False


def victory_for(board, sign):
    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game
    for row in range(len(board)):
        print("printing row", board[row])
        if ['X', 'X', 'X'] == board[row] or ['O', 'O', 'O'] == board[row]: # temporary siimplification; will seperate player/computer winning condition later
            return True
        else:
            return False

def draw_move(board):
    # The function draws the computer's move and updates the board.
    from random import randrange
    computer_move = randrange(1,10)

    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == computer_move:
                move_coordinates = (row, column)
                if make_list_of_free_fields(board, move_coordinates) == True: # check if field is free
                    board[row][column] = 'X'
                else:
                    draw_move(board)
    return board


board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]
sign = False
while victory_for(board, sign) == False:
    display_board(board)
    print(board)
    enter_move(board)
    display_board(board)
    print(board)
    victory_for(board, sign)
    draw_move(board)
    display_board(board)
    victory_for(board, sign)
print("Game Over")