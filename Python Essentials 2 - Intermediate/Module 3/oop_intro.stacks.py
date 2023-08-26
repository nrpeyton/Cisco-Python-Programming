# Defining a class called Stack, representing a simple stack data structure
class Stack:
    # Constructor method, initializing an empty stack list
    def __init__(self):
        self.__stack_list = []  # Private variable, thanks to double underscores, storing the elements of the stack

    # Method to add (push) an item to the stack
    def push(self, val):
        self.__stack_list.append(val)  # Appending the value to the stack

    # Method to remove (pop) an item from the stack
    def pop(self):
        val = self.__stack_list[-1]  # Retrieving the last value in the stack
        del self.__stack_list[-1]    # Deleting the last value from the stack
        return val                   # Returning the popped value


# Defining a class called AddingStack, inheriting from the Stack class
class AddingStack(Stack):
    # Constructor method, initializing the base Stack and an additional sum variable
    def __init__(self):
        Stack.__init__(self)  # Calling the constructor of the base Stack class
        self.__sum = 0        # Private variable to store the sum of the elements in the stack

    # Method to get the current sum of the elements in the stack
    def get_sum(self):
        return self.__sum     # Returning the sum

    # Method to add (push) an item to the stack while updating the sum
    def push(self, val):
        self.__sum += val     # Increasing the sum
        Stack.push(self, val) # Calling the push method of the base Stack class

    # Method to remove (pop) an item from the stack while updating the sum
    def pop(self):
        val = Stack.pop(self) # Calling the pop method of the base Stack class
        self.__sum -= val     # Decreasing the sum
        return val            # Returning the popped value


# Creating an object of the AddingStack class
stack_object = AddingStack()

# Pushing values 0 through 4 onto the stack
for i in range(5):
    stack_object.push(i)

print("Sum:", stack_object.get_sum()) # Printing the sum of the stack

# Popping values from the stack and printing them
for i in range(5):
    print(stack_object.pop())



''' OUTPUTS:

Sum: 10
4
3
2
1
0

'''