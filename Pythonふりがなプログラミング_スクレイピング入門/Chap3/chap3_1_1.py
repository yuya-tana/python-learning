from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
lists = soup.select(
    '#ToolList > ul > li > div > a ')
for list in lists:
    list_name = list.get_text(strip=True)
    list_url = urljoin(url, list['href'])
    print(list_name)
    print(list_url)

# get_text属性を使って文字を抜き出すことで、タグの情報だったり不要となるものを取り除いた状態で出力される。また、引数として'-'と指定すると、文字列の間に指定した-が挿入されたりもする。