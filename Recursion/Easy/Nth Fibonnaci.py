# Recursive Solution
def getNthFib(n):
    if n == 1 or n == 2:
        return n - 1

    return getNthFib(n - 1) + getNthFib(n - 2)


# Iterative Solution
def getNthFib(n):
    if n == 1 or n == 2:
        return n - 1

    a = 0
    b = 1
    num = 0

    for idx in range(n-2):
        num = a + b
        a = b
        b = num

    return num
