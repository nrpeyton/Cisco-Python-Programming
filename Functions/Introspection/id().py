id(object)

"""
Returns the “identity” of an object. This is the address of the object in memory; an integer which is guaranteed to be unique and constant.
"""




list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list2 = list1

print(id(list1), id(list2)) # Output: IDs match.