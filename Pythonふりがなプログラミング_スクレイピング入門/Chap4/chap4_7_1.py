import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
df_m = df.query('月1 >= 150')
print(df_m)