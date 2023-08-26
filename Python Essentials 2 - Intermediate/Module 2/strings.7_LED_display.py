'''                                         2.4.1.6 LAB: A LED Display

This was meant to simulate an old 7 segment LED display (as used on old alarm clocks etc), but implimented here instead
with 15 LEDs (as #) on a 5x3 grid.

All core functionality is present, but stopped after configuring digits 1, 2, & 3 only to save time.

Began by creating digital patterns but didn't need them.  Left them incase of core change to implimentation in future.
'''

# digit_patterns = ['0010100101001', #1    ***** NOT USED *****
# '1110111110111', #2
# '1110111101111'] #3


  # ### ### # # ### ### ### ### ### ### 
  #   #   # # # #   #     # # # # # # # 
  # ### ### ### ### ###   # ### ### # # 
  # #     #   #   # # #   # # #   # # # 
  # ### ###   # ### ###   # ### ### ###


def led_processor(input):
    
    line_print_1 = line_print_2 = line_print_3 = line_print_4 = line_print_5 = '' # one line initialisation
        
    for d in input:
        
        grid = [] # re-initialise grid for each digit:
        
        for row in range(5): # Create two dimensional 5x3 grid (5 rows, each with 3 columns)
            column = [' ' for i in range(3)] #  "OFF LED" represented by space ' '
            grid.append(column)
        
         # activate digit's LED pattern
        if d == '1':
            grid[0][2] = grid[1][2] = grid[2][2] = grid[3][2] = grid[4][2] = '#'
            
        elif d == '2':
            grid[0][0] = grid[0][1] = grid[0][2] = '#'
            grid[1][2] = '#'
            grid[2][0] = grid[2][1] = grid[2][2] = '#'
            grid[3][0] = '#'
            grid[4][0] = grid[4][1] = grid[4][2] = '#'
            
        elif d == '3':
            grid[0][0] = grid[0][1] = grid[0][2] = '#'
            grid[1][2] = '#'
            grid[2][0] = grid[2][1] = grid[2][2] = '#'
            grid[3][2] = '#'
            grid[4][0] = grid[4][1] = grid[4][2] = '#'
            
        line_print_1 += ' ' + "".join(grid[0]) # joins list of top 3 LED status lights (represented as 'space' or '#') into one string
        line_print_2 += ' ' + "".join(grid[1]) # same as above, but for next line
        line_print_3 += ' ' + "".join(grid[2]) # and so on...
        line_print_4 += ' ' + "".join(grid[3])
        line_print_5 += ' ' + "".join(grid[4])
    
    all_line_print = line_print_1 + '\n' + line_print_2 + '\n' + line_print_3 + '\n' + line_print_4 + '\n' + line_print_5
    
    return all_line_print
print(led_processor('12233311')) #    * * *    I N P U T    * * *

'''
OUTPUTS:

   # ### ### ### ### ###   #   #
   #   #   #   #   #   #   #   #
   # ### ### ### ### ###   #   #
   # #   #     #   #   #   #   #
   # ### ### ### ### ###   #   #
   
'''











# join() method examples purely for self-reminder/future reference:
# string = " ".join(["omicron", "pi", "rho"]) # outputs: 'omicron pi rho'
# string = ",".join(["omicron", "pi", "rho"]) # outputs: 'omicron,pi,rho'