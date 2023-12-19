from pathlib import Path
import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
df['合計'] = df[['月1', '月2', '月3',]].sum(axis=1)
print(df)

efile = Path ('bsaleses.csv')
#efile.write_text(df, encoding='utf-8')
df.to_csv(efile, encoding='utf-8')

# 合計行を追加しちゃったりなんかするコード