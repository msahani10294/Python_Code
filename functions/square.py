def square(n):
    return n**2


def square_nos(n):
    if n > 0:
        squareList = list(map(square, range(1, n+1)))
    else:
        return "invalid input please enter a valid input"
    return squareList


print(square_nos(10))
