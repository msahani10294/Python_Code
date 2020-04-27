n = int(input("Enter a range of no : "))
l = list(range(1,n+1))

square = []

for i in l:
    if i >= 0:
        square.append(i**2)
print(square)