import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
df['合計'] = df[['月1', '月2', '月3',]].sum(axis=1)
print(df)

# 合計行を追加しちゃったりなんかするコード