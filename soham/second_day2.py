import numpy as np

arr = np.array([[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10]])
arr1 = np.array([[[1, 2, 3], [4, 5, 6]],
                 [[7, 8, 9], [10, 12, 11]]])
print(arr1.ndim)

print(arr.shape)
print(arr.dtype)
print(arr.itemsize)
print(arr.size)
print(arr1[:, 0])
print(np.zeros((3, 3)))
print(np.ones((3, 3)))
print(np.ones((4, 2, 2), dtype='int32'))

print(np.random.randint(-4, 2, size=(3, 3)))
print(np.identity(3))
