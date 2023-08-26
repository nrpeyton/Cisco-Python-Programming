# 4.3.1.9 LAB: Prime numbers - how to find them

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
            
    sqrt_of_num = int(num ** 0.5)
    for i in range(sqrt_of_num):
        i += 1
        if num % i == 0:
            return True
        else:
            return False

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()