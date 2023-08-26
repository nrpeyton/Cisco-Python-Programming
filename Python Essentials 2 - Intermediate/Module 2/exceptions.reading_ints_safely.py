def read_int(prompt, min, max):
    condition = False
   
    while condition == False:

        try:
            st = int(input(prompt))
            assert st >= min and st <= max
            return st
            condition = True
        except ValueError:
            print("Error: wrong input")
        except AssertionError:
            print("Error: the value is not within permitted range (-10..10)")


v = read_int("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)

