import pandas as pd

pd.set_option('display.unicode.east_asian_width',True)
df = pd.read_csv('bsales.csv', encoding='utf-8')
month1_sum = df['月1'].sum()
print(month1_sum)

# そのほか、max,minなどなどが使えたりもする。