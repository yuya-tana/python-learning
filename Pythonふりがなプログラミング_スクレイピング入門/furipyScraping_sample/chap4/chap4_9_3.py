import pandas as pd

df = pd.read_csv('bsales.csv', encoding='utf-8')
keywords = ['Python', 'Ruby', 'Java']
for keyword in keywords:
    df_k = df.query('書名.str.contains(@keyword)')
    print(keyword, len(df_k))
