def decor(num):
    def inner():
        a = num()
        print("======")
        return a

    return inner


@decor
def num():
    return 10


# result_fun = decor(num)
# print(result_fun())

print(num())