import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
col_book = df['書名']
row_0 = df.iloc[0]
print(row_0)