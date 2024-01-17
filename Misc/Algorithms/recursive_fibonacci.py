def fib(n):
    if n < 3: return 1
    return fib(n-1) + fib(n-2)

print(fib(int(input('Enter Fib Index: '))))

# def fib(n, memo={}):
#     if n in memo:
#         return memo[n]
#     if n < 3: 
#         return 1
#     memo[n] = fib(n-1, memo) + fib(n-2, memo)
#     return memo[n]

# print(fib(50))


