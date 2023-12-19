import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bcount.csv', encoding='utf-8')
df.plot.bar(x='classification', y='count', rot=45)
plt.savefig('barplotfig.png')