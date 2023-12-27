EMPTY = "------"
CASTLE = "CASTLE"
PAWN = "-PAWN-"
board = []

for i in range(8):
    row = [EMPTY for i in range(8)]
    board.append(row)

board[0][0] = CASTLE
board[0][7] = CASTLE
board[7][0] = CASTLE
board[7][7] = CASTLE

board[3][4] = PAWN

print(board)

print('\n')
for r in board:
    print('\n', r)