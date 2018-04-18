# 911.csv from: https://www.kaggle.com/lawin2593/911-analysis/data
# Code adapted from: https://www.kaggle.com/vadim0912/911-calls-visualization

import matplotlib.pyplot as plt

# pyplot Sample
plt.plot([1,2,3,4], [1,4,9,1], 'bo')
plt.axis([0, 6, 0, 20])
plt.show()

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('~/911/911.csv')
df.head()

# Sample the data so the graph is more readable as opposed to all smeared as dots
df = df.sample(n=1000) 

plt.plot(df['lat'], df['lng'], 'bo')
plt.axis([min(df['lat']), max(df['lat']), min(df['lng']), max(df['lng'])])
plt.show()


