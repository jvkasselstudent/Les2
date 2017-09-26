import time


def double(num):
    return num * 2


b = 7
b = double(b)

print(b)

print(time.strftime("%H:%M:%S"))


def f(y):
    return 2 * y + 1


def g(x):
    return 5 + x + 10


print(f(3) + g(3))
