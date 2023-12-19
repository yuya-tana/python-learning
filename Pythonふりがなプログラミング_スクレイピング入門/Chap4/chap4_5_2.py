import pandas as pd

dfs = pd.read_html('book.html', encoding='utf-8')
print(dfs)