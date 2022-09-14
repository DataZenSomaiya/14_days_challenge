import numpy as np

# 2D Array
arr1 = np.array([[9.0,8.0,7.0,5.0,9.0],[6.0,5.0,4.0,7.8,6.9]])
print(arr1)


arr2 = np.array([[9.0,8.0,7.0,5.0,9.0,4.0,3.2,7.9],[6.0,5.0,4.0]], dtype =object)
print(arr2)

print('\n')
# Get Dimension
print('Dimension of Array 1-',arr1.ndim)
print('Dimension of Array 2-',arr2.ndim)

print('\n')
# Get Shape
print('Shape of Array 1-',arr1.shape)
print('Shape of Array 2-',arr2.shape)

print('\n')
# Get Type
print('Type of Array 1-',arr1.dtype)
print('Type of Array 2-',arr2.dtype)

print('\n')
# Get Size
print('Size ',arr1.itemsize)

print('\n')
# Get number of elements
print('number of elements ',arr1.size)

print('\n')
# Get a specific element [r, c]
print('specific element [r, c]')
print(arr1[0, 2])

print('\n')
# Get a specific row
print('specific row')
print(arr1[0, :])

print('\n')
# Get a specific column
print('specific column')
print(arr1[:, 2])

print('\n')
# Getting a little more fancy [startindex:endindex:stepsize]
print('startindex:endindex:stepsize')
print(arr1[0, 1:-1:2])