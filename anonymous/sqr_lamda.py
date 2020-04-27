n = int(input("enter a nos :"))
l = list(range(1,n+1))

sqr_no = list(map(lambda x:x**2, l))
print(sqr_no)