from os import strerror

# Initialise 10 bytes in a bytearray, fill each byte with a number from 10 to 19, then write to a file.

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('byte_file.bin', 'wb')
    bf.write(data)
    bf.close()
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))





# Reads bytes from the stream in hex.

try:
    bf = open('byte_file.bin', 'rb')
    data = bytearray(bf.read())
    bf.close()

    for b in data:
        print(b, end=' ')
        print(hex(b))

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))





# Reads only 4 bytes from the stream
print('\n')

try:
    bf = open('byte_file.bin', 'rb')
    data = bytearray(bf.read(4)) # <--- only change read(4)
    bf.close()

    for b in data:
        print(b, end=' ')
        print(hex(b))

except IOError as e:
    print("I/O error occurred:", strerror(e.errno))