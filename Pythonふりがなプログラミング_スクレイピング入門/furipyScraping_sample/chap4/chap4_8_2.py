import pandas as pd

pd.set_option('display.unicode.east_asian_width',
              True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
v_mean = df['月3'].mean()
df_f = df['月3'].fillna(v_mean)
print(df_f)
