import pandas as pd
import numpy as np
data = {'name': ['SHreya', 'Apeksha', 'D', 'G'],
        'age': ['10', '40', '17', '6'],
        'score': [9.4, 8.9, 7.2, 9]}
df = pd.DataFrame(data)
print (df)
print(df.head(2))
