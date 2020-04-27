n = int(input("enter a no range: "))
l = list(range(1, n+1))
even = [i for i in l if i%2==0]
print(even)