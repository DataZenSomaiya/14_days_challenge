# -*- coding: utf-8 -*-
"""Day 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FNTAD7ZCu3WEyKoQcSUnrS3DVVKGDVB5
"""

import matplotlib.pyplot as plt
import numpy as np

price = [100, 250, 310, 600, 850]
size = [1000, 2300, 3000, 5700, 8100]

plt.scatter(size, price, color = 'black')
plt.ylabel('price')
plt.xlabel('size')
plt.show()

