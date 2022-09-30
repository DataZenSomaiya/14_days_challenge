import pandas as pd
import numpy as np

#Trying and testing out numpy and pandas by creating a dataframe

#Creating a DataFrame
data = {'Brand': ['Ford', 'Toyota', 'Honda', 'Subaru'],
        'model' : ['Mustang', 'Supura', 'Accord', 'Ascent'],
        'year' : [1994, 1999, 1995, 2022] }

df = pd.Dataframe(data)

## Parameters ##
## Data : ndarray (Structured or homogeneous), Iterable, dict, or DataFrame
## Index : The index (row labels) of the DataFrame
## Columns : The column labels of the DataFrame
## dtype
## copy