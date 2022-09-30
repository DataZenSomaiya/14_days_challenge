#!/usr/bin/env python
# coding: utf-8

# In[2]:


import requests
response = requests.get('https://divyatutorials718242806.wordpress.com')
print(response)
print(response.url)

