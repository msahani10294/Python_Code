l = [1, 3, 56, 67, 87, 45]
x = [76,77,78]
# append adds its argument as a single element to the end of a list.
# The length of the list itself will increase by one.
print(l)
l.append(x)
print(l)


# extend iterates over its argument adding each element to the list, extending the list.
# The length of the list will increase by however many elements were in the iterable argument.
l.extend([5])
print(l)

l.extend(x)
print(l)
