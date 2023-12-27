class Cats():
    def __init__(self):
        self.cat_list  = ['bob', 'tigre', 'charlie']
        self.n = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if len(self.cat_list) == self.n:
            raise StopIteration
        
        self.n += 1
        return self.cat_list[self.n - 1]

obj = Cats()

for i in obj:
    print (i)







class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration

""" After instantiating SequenceIterator, Python prepares the sequence object for iteration by calling its .__iter__() method. This method returns 
the actual iterator object. Then, the loop repeatedly calls .__next__() on the iterator to retrieve values from it.  
How the 'for' loop works internally is shown below."""
for i in SequenceIterator([1, 2, 3, 4, 5]): 
    print(i, end='') # Outputs: 12345




# HOW PYTHON'S FOR LOOPS WORK INTERNALLY
sequence = SequenceIterator([1, 2, 3, 4, 5])

# Get an iterator over the data
iterator = sequence.__iter__()
while True:
    try:
        # Retrieve the next item
        item = iterator.__next__()
    except StopIteration:
        break
    else:
        # The loop's code block goes here...
        print(item)





# The hardest part to comprehend is how simply having __iter__ return 'self' results in the "miraculous" call of __next__.
# We can explain whats happening below.  We'll copy the entire SequenceIterator class from above, but comment out the __iter__ method and replace the 'for' loop with the two lines below**.

class SequenceIterator:
    def __init__(self, sequence):
        self._sequence = sequence
        self._index = 0

    #def __iter__(self):
    #    return self

    def __next__(self):
        if self._index < len(self._sequence):
            item = self._sequence[self._index]
            self._index += 1
            return item
        else:
            raise StopIteration
        
# ***
obj = SequenceIterator([1, 2, 3, 4, 5]) # Get our object manually instead of calling __iter__()
print(obj.__next__()) # Output: 1       # Call __next__ on our object manually instead of a 'for' loop doing it; 
                                        #   with the __iter__ function commented out, this code here still works.  This is because we've manually got our object (obj) so we can call '__next__ on it.  This is iter's reason to exist and return 'self', it gets the object so that __next__ can be called on it.







                                        