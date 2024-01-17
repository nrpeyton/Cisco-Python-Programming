def calculate_average(file_path):
    try:
        f = open(file_path, 'r')
        linesList = f.readlines()
    except FileNotFoundError as e:
        return str(e)
    finally:
        f.close()

    sum = 0
    cnt = 0
    
    for line in linesList:
        try:
            sum += float(line)
            cnt += 1
        except ValueError as e:
            continue

    if cnt > 0: return sum / cnt

# Example usage
print(calculate_average("numbers.txt"))  # Assuming numbers.txt contains a list of numbers



dic = {'name': 'bob', 'age': 20}
print(dic)







import platform

if platform.python_version_tuple()[0] == '3' and int(platform.python_version_tuple()[1]) > 8 and 'x86_64' in platform.platform():
    print('Environment suitable')
else:
    print('Environment not suitable: requires Python 3.8 and a 64 bit CPU')


import platform

import platform

if platform.system() == 'Windows':
    print('Your windows version is: ', platform.platform())
elif platform.system() == 'Linux':
    print('Your Linux kernel version is', platform.platform(), 'and your Linux distribution is: ', platform.version())





def factorial(n, result = 1):
    
    for i in range(1, n+1):
        result *= i
                    
    return result

print("The value of 5! should be " + str(5*4*3*2*1))
print("The value of 5! is " + str(factorial(5)))
print("The value of 0! should be 1")
print("The value of 0! is " + str(factorial(0)))


assert factorial(5) == 120, "The value of 5! should be 120"
assert factorial(0) == 1, "The value of 0! should be 1"






print('ASCII   Character   Types')
for i in range(ord(chr(32)), ord(chr(128))):
    print(i, chr(i), 'isalnum()' if chr(i).isalnum() == True else '',  'isalpha()' if chr(i).isalpha() == True else '',  'isdigit()' if chr(i).isdigit() == True else '',  'isdecimal()' if chr(i).isdecimal() == True else '',  'isnumeric()' if chr(i).isnumeric() == True else '', 'isspace()' if chr(i).isspace() == True else '', sep="         ")
