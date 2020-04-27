import math
n = int(input("how many no you want to add : "))
l = []
j = 1
for i in range(n):
    number = int(input("enter {} no :".format(j)))
    l.append(number)
    j+=1
print(sum(l))