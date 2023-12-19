import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
df_dna = df.dropna()
print(df_dna)

# 欠損値が存在する行ごと削除してしまう関数
