# import platform
# pl = platform.platform()
# m = platform.machine()
# pr = platform.processor()
# v = platform.version()
# s = platform.system()


# print('platform.platform:', pl)
# print('platform.machine:', m)
# print('platform.processor:', pr)
# print('platform.version:', v)
# print('platform.system:', s)

file_name = 'line_count.txt'
data = "Line1\\nLine2\\nLine3"

# Write data to the file
file = open(file_name, 'w')
file.write(data)
file.close()

# Read the file and count the lines
file = open(file_name, 'r')
line_count = 0
for line in file:
    line_count += 1
file.close()

print(line_count)
