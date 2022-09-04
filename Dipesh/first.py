import pandas as pd
import matplotlib.pyplot as plt

# Read the csv file
data_2={'name': ['Jay', 'Dipesh', 'Ud', 'Rd'],
        'age': ['22', '22', '21', '23'],
        'score': [9.4, 9.09, 9.2, 9]}
df = pd.DataFrame(data_2)

## Parameters ##
## Data : ndarray (structured or homogeneous), Iterable, dict, or DataFrame
## index: The index (row labels) of the DataFrame.
## columns: The column labels of the DataFrame.
## dtype
## copy

df.to_csv('file1.csv', index= False)

print(df)