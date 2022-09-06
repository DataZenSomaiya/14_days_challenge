#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np


# In[4]:


arr1 = np.array([[1,2,3,4,5],[6,7,8,9,21]])
print(arr1)

arr2 = np.array([[5,4,3,2,1],[3,4,5,7,11]], dtype =object)
print(arr2)


# In[6]:



print('Dimension of Array 1-',arr1.ndim)
print('Dimension of Array 2-',arr2.ndim)


print('Shape of Array 1-',arr1.shape)
print('Shape of Array 2-',arr2.shape)


print('Type of Array 1-',arr1.dtype)
print('Type of Array 2-',arr2.dtype)


print('Size ',arr1.itemsize)


print('Number of elements ',arr1.size)


# In[9]:


print(arr1[0, 2])

print(arr1[0, :])

print(arr1[:, 2])

print(arr1[0, 1:-1:2])


# In[10]:



print(np.zeros((1,3)))
print('*'*5)

print(np.ones((5,2,2), dtype='int32'))
print('*'*5)

# Any other number
print(np.full((4,3,2), 99, dtype='int32'))
print('*'*5)


# In[11]:



print(np.random.rand(5,2))


print(np.random.randint(-4,8, size=(3,3)))


print(np.identity(5))


# In[12]:


np.mean(arr1)


# In[13]:


np.mean(arr2)


# In[14]:


np.max(arr1)


# In[15]:


np.std(arr1)


# In[ ]:




