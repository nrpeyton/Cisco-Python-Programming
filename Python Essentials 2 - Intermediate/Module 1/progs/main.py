import module

zeroes = [0 for i in range(5)]
ones = [1 for i in range(5)]
print(module.suml(zeroes))
print(module.prodl(ones))

print(module.__counter)




# although not required in this script, non-standard packages can be added to the path with:
from sys import path
path.append('../packages') #...which improves portability as long as the relative paths are kept.
print(path)
