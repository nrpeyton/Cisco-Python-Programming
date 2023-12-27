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