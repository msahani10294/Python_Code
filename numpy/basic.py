import numpy as np

np_list = np.array(
    [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
)

print(np_list.shape)
print(np_list.size)
print(type(np_list))
print(np_list.reshape(3,3))
print(np_list.flatten())

print(np_list.max())
