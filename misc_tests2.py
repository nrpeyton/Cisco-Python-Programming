import errno
                                        # file.txt exists and was created using the next three lines:
f = open('file.txt', 'w+')
f.write('line 1\nline 2\nline 3\nline 4')
f.close()

f = open('file.txt', 'a+')
f.seek(0)
s2 = f.read()
f.close()
# f.seek(0)
# s1 = f.read() + '    ...first read'      # reads succesfully
# f.write('new line')                      # ignores seek() and (successfully) appends the string at the end
# s2 = f.read() + '    ...second read'     # nothing is read, because the 'a' mode "forced" write() to moved the head to the end before writing
# f.close()
# print(s1)
print(s2)

# Always remember to re-position the head using seek() after a write operation in 'append & read' (a+) mode.

from platform import platform

print(platform())

class A:
    def __init__(self):
        pass
    

print(A.__module__)
print(A.__name__)
print(A.__init__.__module__)