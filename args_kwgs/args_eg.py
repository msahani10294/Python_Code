# args is variable length argument
# type of args is tuple


def greet(*args):

    print(type(args))
    for i in args:
        print("HI !", i)


greet("Good Morning", "Hello ", "Good night")