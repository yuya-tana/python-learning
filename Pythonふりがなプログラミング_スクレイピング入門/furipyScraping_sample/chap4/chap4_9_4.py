import pandas as pd

df = pd.read_csv('bsales.csv', encoding='utf-8')
keywords = ['Python', 'Ruby', 'Java']
book_list = []
for keyword in keywords:
    df_k = df.query('書名.str.contains(@keyword)')
    book_list.append([keyword, len(df_k)])
print(book_list)
df = pd.DataFrame(book_list, columns=
                  ['classification', 'count'])
df.to_csv('bcount.csv', index=False)
