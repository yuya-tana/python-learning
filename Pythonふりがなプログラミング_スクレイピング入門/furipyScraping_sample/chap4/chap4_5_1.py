import pandas as pd

dfs = pd.read_html('book.html', encoding='utf-8')
dfs[0].to_csv('bsales.csv', index=False)
