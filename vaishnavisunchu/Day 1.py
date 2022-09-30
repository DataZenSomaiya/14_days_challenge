import pandas as pd
import numpy as np

## 1. Creating a DataFrame.
data = {'name': ['Jay', 'Ron', 'joe', 'Ross'],
        'age': ['5', '10', '7', '6'],
        'score': [9.4, 8.9, 7.2, 9]} 

df = pd.DataFrame(data)

## Parameters ##
## Data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
## index: The index (row labels) of the DataFrame.
## columns: The column labels of the DataFrame.
## dtype
## copy

df.to_csv('C:\\Users\\sairajsunchu\\desktop\\VaishnaviSunchu_14_days_challenge\\14_days_challenge\\text_csv', index= False)
print(df)