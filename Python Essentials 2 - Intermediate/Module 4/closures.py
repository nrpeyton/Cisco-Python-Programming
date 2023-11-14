'''
A closure in Python is a function that retains access to variables from its surrounding environment, even after the outer function, where it was defined, has 
finished execution.
'''

def tag(tg):
    tg2 = tg[0] + '/' + tg[1:]

    # Define the inner function 'inner'
    def inner(str):
        return tg + str + tg2
    return inner # Return a reference to the inner function (not calling it, hence no parentheses)


b_tag = tag('<b>') # Call 'tag' with argument '<b>', and store the returned function reference in 'b_tag'
print(b_tag('Monty Python')) # Now call the function referenced by 'b_tag', passing 'Monty Python' as argument

# Outputs: <b>Monty Python</b>
