import numpy as np

a = np.array(
    [
        [1, 2],
        [4, 5]
    ])

b = np.array(
    [
        [7, 8],
        [10, 11]
    ])

# sum of two array
sum = a+b
print(sum)

# Array multiplication

mul = a*b
print(mul)

# matrix multiplication

m_mult = a.dot(b)
print(m_mult)