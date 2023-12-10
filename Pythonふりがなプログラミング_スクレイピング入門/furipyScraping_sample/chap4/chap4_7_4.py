import pandas as pd

pd.set_option('display.unicode.east_asian_width',
              True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
df_ap = df.query('分類 in ["AI", "パソコン"]')
print(df_ap)
