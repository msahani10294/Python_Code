from numpy import *
# there are multiple way to create an array
# 1. array()

arr1 = array([1, 2, 4, 5])
print(arr1)

# 2. linespace()
arr2 = linspace(0, 5, 6)
print(arr2)

# 3. logspace()
arr3 = logspace(10, 40,2)
print(arr3)

# arrange
arr4 = arange(1, 10)
print(arr4)

# 5. zeros()
arr5 = zeros(3)
print(arr5)

# 6. ones()
arr6 = ones(5)
print(arr6)

print(arr1.__sub__(5))
