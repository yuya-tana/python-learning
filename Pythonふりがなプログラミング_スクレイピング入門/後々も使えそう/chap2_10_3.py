from pathlib import Path
import requests
from bs4 import BeautifulSoup

url = 'https://yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
lists = soup.select(
    '#ToolList > ul > li > div > a ')
btext = ''
for list in lists:
    btext += list.text
    btext += '\n'
efile = Path ('top5books.txt')
efile.write_text(btext, encoding='utf-8')

#ToolList > ul > li:nth-child(1) > div > a
#> li:nth-of-type(1) > div > a

# 抜き出してきた内容をテキストファイルに保存してあげる一連のコードｖ　いい感じになってきたで！！このままだと上書きされるので、追記はまた別でやる必要がある。