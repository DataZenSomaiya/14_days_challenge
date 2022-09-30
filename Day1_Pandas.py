#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data = {'name': ['Paarth','Peppur','Saloni'],
        'age': [20,4,26],
        'score': [9., 8, 7]} 

df = pd.DataFrame(data)


# In[6]:


df.to_csv('C:\\Users\\paart\\text.csv', index= False)
print(df)


# In[7]:


df1 = pd.read_csv('C:\\Users\\paart\\text.csv')
df1


# In[8]:


dfr = pd.read_csv('C:\\Users\\paart\\TataSteel_HistoricData.csv')
dfr


# In[9]:


rows, columns = dfr.shape
print('Number of rows',rows)
print('Number of columns',columns)


# In[11]:



print(dfr.head(5))


print(dfr.tail(3))


# In[12]:


print(dfr.iloc[0])
print(dfr.iloc[0,0:3])


# In[13]:


dfr.describe()


# In[ ]:




