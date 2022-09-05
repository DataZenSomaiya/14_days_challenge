import pandas as pd
import numpy as np

data = {'name': ['Ram', 'Shyam', 'Ghanshyam', 'Madhuram'],
        'age': ['21', '24', '27', '22'],
        'score': [9.4, 9.5, 8.7, 7.6]}

df = pd.DataFrame(data)
df.to_csv('C:\\Users\\DELL\\14_days_challenge\\jaswant\\text_csv', index=False)
print(df)

df_read = pd.read_csv('C:\\Users\\DELL\\14_days_challenge\\jaswant\\text_csv')
print(df_read)
