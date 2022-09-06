import pandas as pd
import numpy as np

df=pd.read_csv('C:\\Users\\adity\\OneDrive\\Desktop\\numpy\\TataSteel_HistoricData[1745].csv')
print(df)

rows,columns=df.shape
print('rows',rows)
print('columns',columns)

print(df.head(4))
print(df.tail(2))

print(df.iloc[0])
print(df.iloc[0,0:2])

df.describe()



arr1 = np.array([[9.0,7.0,19.0,7.0,8.0],[8.0,9.0,5.0,7.8,4.9]])
print(arr1)

arr2 = np.array([[8.0,6.0,5.0,4.0,3.0,2.0,1.2,8.9],[7.0,6.0,2.0]], dtype =object)
print(arr2)

print(arr1[0, 3])

 
print(arr1[0, :])

print(arr1[:, 3])


print(arr1[0, 2:-1:2])



print(np.zeros((3,3)))

print(np.ones((3,2,1), dtype='int32'))
print('*'*25)

print(np.full((4,3,1), 99, dtype='int32'))
print('*'*25)


print(np.random.rand(6,4))


print(np.random.randint(-3,7, size=(2,2)))

print(np.identity(4))



