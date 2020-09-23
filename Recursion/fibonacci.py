
# 1,1,2,3,5,8,13


def fib(n):
    if n >= 3:
        return fib(n - 1) + fib(n - 2)
    return 1


for i in range(10):
    print(fib(i))
