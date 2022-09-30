import pandas as pd


df = pd.read_csv('E:\\Github\\14_days_challenge\\soham\\Tata_Data.csv')

print(df)
rows, columns = df.shape

print('Rows are : ', rows)
print('Columns are : ', columns)
print(df.head(3))
print(df.tail(3))
print(df.iloc[0, 4])
df.describe()
