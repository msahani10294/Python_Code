# difference between count and index

l = [1, 2, 3, 4, 5, 6]

count = l.count(10)
# count return 0 if no item found in your list otherwise it return index no of that item
print(count)

# it return index no and if there is no item in your list it raises an error
index1 = l.index(3)
print(index1)

index2 = l.index(10)
print(index2)