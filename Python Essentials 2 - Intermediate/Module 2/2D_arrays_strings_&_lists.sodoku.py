
'''                                     2.5.1.11 LAB: Sudoku

Difficulty: Hard

Objectives:
- Operate with strings and lists.
- Convert strings into lists.

Scenario:
Write a program to validate a 9x9 Sudoku board. The board must meet the following conditions:
- Each row must contain all digits from 0 to 9.
- Each column must contain all digits from 0 to 9.
- Each of the nine 3x3 sub-squares must contain all digits from 0 to 9.

Input:
- 9 rows of 9 digits each.  (Test data moved to lines 97-115)

Output:
- Print 'Yes' if the Sudoku is valid, 'No' otherwise.

'''


def sodoku(fill):
    z = 0
    good_row_counter = 0
    good_column_counter = 0
    good_subsq_counter = 0
    
    fill2 = ''     # FORMAT INPUT
    for c in fill:
        d = c.replace('\n', '')
        fill2 += d

    
    board = [['' for x in range(9)]for x in range(9)]     # BOARD SETUP

    for x in range(9):     # FILL BOARD
        for y in range(9):
                board[x][y] = fill2[z]
                z += 1

    for i in range(9):
        print(board[i])

    for i in range(9):      # CHECK ROWS
        if checker(board[i]) == True:      # Check if the row is 'good'
            good_row_counter += 1
    
    print(board)
    
    for i in range(9):     # CHECK COLUMNS
        list_of_column = []     # reset for each column
        for c in board:
            list_of_column.append(c[i])
        if checker(list_of_column) == True:      # Check if the column is 'good'
            good_column_counter += 1
        

                #     C H E C K   3 x 3   S U B - S Q U A R E S

    for row in range(0, 9, 3):         # Iterate through the board 3 rows at a time
        
        for col in range(0, 9, 3):         # Iterate through the board 3 columns at a time
            subsq = []
            
            for i in range(row, row + 3):     # Capture the elements of the current 3x3 sub-square
                for j in range(col, col + 3):
                    subsq.append(board[i][j])
                    
            if checker(subsq):                 # Check if the sub-square is 'good'
                good_subsq_counter += 1
    
                # RETURN SUDOKU: VALID OR NOT
    print("good row counter:", good_row_counter, "  good column counter:", good_column_counter, "  good sub-square counter: ", good_subsq_counter)
    if good_row_counter == 9 and good_column_counter == 9 and good_subsq_counter == 9:
        return "Yes, Sudoku is valid"
    else:
        return "No Sudoku is not valid"


def checker(row_or_col): # receives list, sorts and checks for all digits 1 to 9. Used by the following code blocks: 'CHECK ROWS', 'CHECK COLUMNS' and 'C H E C K   3 x 3   S U B - S Q U A R E S'
    rc_copy = row_or_col[:]
    rc_copy.sort()
    counter = 0
    
    for i in range(9):
        if int(rc_copy[i]) == i + 1:
            counter += 1
    if counter == 9:
        return True
    else:
        return False


print(sodoku('''295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672''')) # test data: returns yes ✓

print(sodoku('''195743862
431865927
876192543
387459216
612387495
549216738
763524189
928671354
254938671''')) # test data: returns no ✓



'''                                         PERSONAL NOTES / TAKEAWAYS

Only place I needed a little guidance was making my sub-squares block more concise (i.e., lines 63 to 69); see *EXAMPLE below.

double list[x:x][x:x] slicing to access a subarray (i.e., a sub 3x3 sub-square on a 9x9 board) is NOT a thing and does NOT work:
list[x:x][x:x] is treated as:
list[x:x]
list[x:x]
Instead, use list comprehension (preferred) or nested 'for loops'.

if NOT using slices (aka NOT using "index ranges"), double list[x][x] notation is still valid but for accessing single-index values only.
'''

# strings are immutable, their methods don't change them, but they can (and do) return a new string
# the opposite is true for lists, their methods change them in situ, remember to only sort copied slices.


''' *EXAMPLE:
board = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16],
]

for x in range(0, 4, 2):
    for y in range(0, 4, 2):
        subsq = []
        for i in range(x, x + 2):
            for j in range(y, y + 2):
                subsq.append(board[i][j])
        print(subsq)
        
outputs:
[1, 2, 5, 6]
[3, 4, 7, 8]
[9, 10, 13, 14]
[11, 12, 15, 16]
'''