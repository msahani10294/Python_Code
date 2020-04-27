n = int(input("enter a nos :"))
l = list(range(1, n+1))

even_nos = list(filter(lambda x: x % 2 == 0, l))
print(even_nos)