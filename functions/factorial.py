def fact(n):
    prod = 1
    if n == 0:
        return 1

    return n * fact(n-1)


print(fact(5))

