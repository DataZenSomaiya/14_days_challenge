mport numpy as np

arr1 = np.array([[9.0, 8.0, 7.0, 5.0, 9.0], [6.0, 5.0, 4.0, 7.8, 6.9]])
print(arr1)

arr2 = np.array([[9.0, 8.0, 7.0, 5.0, 9.0, 4.0, 3.2, 7.9], [6.0, 5.0, 4.0]], dtype=object)
print(arr2)

# Get Dimension
print('Dimension of Array 1-', arr1.ndim)
print('Dimension of Array 2-', arr2.ndim)

# Get Shape
print('Shape of Array 1-', arr1.shape)
print('Shape of Array 2-', arr2.shape)

# Get Type
print('Type of Array 1-', arr1.dtype)
print('Type of Array 2-', arr2.dtype)

# Get Size
print('Size ', arr1.itemsize)

# Get number of elements
print('number of elements ', arr1.size)

# Get a specific element [r, c]
print(arr1[0, 2])

# Get a specific row
print(arr1[0, :])

# Get a specific column
print(arr1[:, 2])

# Getting a little more fancy [startindex:endindex:stepsize]
print(arr1[0, 1:-1:2])

# All 0s matrix
print(np.zeros((2, 3)))
print('*'*25)

# All 1s matrix
print(np.ones((4, 2, 2), dtype='int32'))
print('*'*25)

# Any other number
print(np.full((2, 3, 2), 99, dtype='int32'))
print('*'*25)

# Random decimal numbers
print(np.random.rand(4, 2))

# Random Integer values
print(np.random.randint(-4, 8, size=(3, 3)))

# The identity matrix
print(np.identity(5))