import pandas as pd
import numpy as np

#Creating a dataframe
data = {'name': ['Jay', 'Ron', 'joe', 'Ross'],
        'age': ['5', '10', '7', '6'],
        'score': [9.4, 8.9, 7.2, 9]}

df = pd.DataFrame(data)

df.to_csv('C:\\Users\\alekh\\pythonProject\\Datazen_DataAnalysis\\text_csv', index=False)
print(df)

#Reading Data from a CSV file
df1 = pd.read_csv('C:\\Users\\alekh\\pythonProject\\Datazen_DataAnalysis\\text_csv')
print(df1)

#Acessing and Manipulating data of a dataframe
df = pd.read_csv('C:\\Users\\alekh\\pythonProject\\Datazen_DataAnalysis\\TataSteel_HistoricData.csv')
print(df)

rows, columns = df.shape
print('rows',rows)
print('columns',columns)

#Head prints first n number of rows
print(df.head(5))

#Head prints first n number of columns
print(df.tail(3))

#Slicing a Dataframe
print(df.iloc[0])
print(df.iloc[0,0:3])

#Descibe
df.describe()