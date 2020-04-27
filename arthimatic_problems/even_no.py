n = int(input("enter a no"))
l = list(range(1,n+1))

even = []
odd = []

for i in l:
    if i % 2 == 0:
        even.append(i)

    else:
        odd.append(i)

print("Even nos are :- ", even)
print("odd no are:- ", odd)