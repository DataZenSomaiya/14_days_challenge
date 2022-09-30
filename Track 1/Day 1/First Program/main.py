import pandas as pd
import numpy as np

data = {'name': ['Jay', 'Ron', 'joe', 'Ross'],
        'age': ['5', '10', '7', '6'],
        'score': [9.4, 8.9, 7.2, 9]} 

df = pd.DataFrame(data)



df.to_csv('C:\\Users\\jayzo\\PycharmProjects\\DataZen_DataAnalysis\\text_csv', index= False)
print(df)
