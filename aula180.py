def factorial(n):
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

print(factorial(10))

n = 10
num = 1
while n >=1:
    num = num*n
    n -= 1

print(num)