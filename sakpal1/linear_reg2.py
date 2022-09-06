import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv("HousingData.csv")
data.head()

data.isnull().sum()
data = data.dropna()

data.isnull().sum() 
data1= data.loc[:,['LSTAT','MEDV']]
data1.head(5)


data.plot(x='LSTAT', y='MEDV', style='o')
plt.xlabel('LSTAT')
plt.ylabel('MEDV')
plt.show()print(y_test_predict)

X = pd.DataFrame(data['LSTAT'])
y = pd.DataFrame(data['MEDV'])

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.3, random_state=1)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
regressor = LinearRegression()
regressor.fit(X_train, y_train)

print(regressor.intercept_)
print(regressor.coef_)

y_train_predict = regressor.predict(X_train)
rmse = (np.sqrt(mean_squared_error(y_train, y_train_predict)))


print("training set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))

print("\n")

y_test_predict = regressor.predict(X_test)
rmse = (np.sqrt(mean_squared_error(y_test, y_test_predict)))


print("The model performance for testing set")
print("--------------------------------------")
print('RMSE is {}'.format(rmse))
print(y_test_predict)