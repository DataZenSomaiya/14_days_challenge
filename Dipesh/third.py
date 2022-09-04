import pandas as pd
df = pd.read_csv('C:\\Users\\wwwde\\14_days_challenge\\Dipesh\\TataSteel.csv')
print(df)

rows, columns = df.shape
print('rows',rows)
print('columns',columns)

## Head prints first n number of rows
print(df.head(5))

print('\n')

## Tail prints lat n number of rows
print(df.tail(3))

print('\n')
print('\n')

## Slicing a Dataframe
print('Slicing')
print(df.iloc[0])
print(df.iloc[0,0:3])

print('\n')

## Descibe
print(df.describe())