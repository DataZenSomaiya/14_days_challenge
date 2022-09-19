import seaborn as sns
from matplotlib import pyplot as plt

x = [5, 56,10, 15, 8.4, 20]
y = [90,78, 40, 35, 5, 55.7]
sex =['M', 'F', 'F', "M", 'F','M']
sns.scatterplot(x=x, y=y, hue=sex)