'''def fib_series(n):
    a = 0
    b = 1
    if n == 1:
        return a
    elif n == 2:
        return b
    else:
        for i in range(2, n+1):
            c = a + b
            a = b
            b = c

        return c


print(fib_series(10))'''

'''l1 = [0, 1, 1]


def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)


print(fib(10))'''

n = int(input("enter a number: "))
l1 = [0, 1]
a = 0
b = 1
if n == 0:
    print("[0]")
elif n == 1:
    print(l1)
else:
    for i in range(2, n+1):
        c = a + b
        a = b
        b = c
        l1.append(c)


print(l1)
