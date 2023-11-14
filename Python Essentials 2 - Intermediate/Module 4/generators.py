'''
First yield: s '+' doubles to s '++' and prints
Second yield: s '++' doubles to s '++++' and prints
'''

def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s


for x in fun(2):
    print(x, end='')

# Output ++++++





def fun(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

gen = fun(2)
print(next(gen)) # Output ++
print(next(gen)) # Output ++++





# A list comprehension becomes a generator when used inside parentheses.  This is more memory efficient then being used inside brackets (see next example):
for x in (el * 2 for el in range(5)):
    print(x)
'''
Output:
0
2
4
6
8
'''




# Less memory efficient than above.
for x in [el * 2 for el in range(5)]:
    print(x)
'''
Output:
0
2
4
6
8
'''





x =  (el * 2 for el in range(5))
print(x) #Output: <generator object <genexpr> at 0x7f0b705642b0>





x =  [el * 2 for el in range(5)]
print(x) #Output: [0, 2, 4, 6, 8]