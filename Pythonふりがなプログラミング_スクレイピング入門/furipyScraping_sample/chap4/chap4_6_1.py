import pandas as pd

pd.set_option('display.unicode.east_asian_width',
              True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
col_book = df['書名']
print(col_book)
