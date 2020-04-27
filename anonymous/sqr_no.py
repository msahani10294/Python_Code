n = int(input("enter a range of nos: "))
l = list(range(1, n+1))


def sqr(x):
    return x**2


def square_no():
    global l
    l = list(map(sqr, l))
    return l

print(square_no())
print(sqr(-10))