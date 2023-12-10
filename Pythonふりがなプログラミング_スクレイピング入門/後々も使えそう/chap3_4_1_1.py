from pathlib import Path
import time
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://www.watch.impress.co.jp/category/business/'
btext = ''
for i in range(1, 4):
    if i == 1:
        page_url = url
    else:
        page_url = urljoin(url, f'index{i}.html')
    res = requests.get(page_url)
    soup = BeautifulSoup(res.text, 'html.parser')
    articles = soup.select('#main > article > section > div > ul > li > div > div.text > p.title > a')
    for article in articles:
        print(f'{i}ページ目', article.text)
        btext += f'{i}ページ目：'
        btext += article.text
        btext += '\n'
    time.sleep(1)
efile = Path ('impress_article.txt')
efile.write_text(btext, encoding='utf-8')

#main > article > section > div > ul > li > div > div.text > p.title > a

# テキストファイルへの追加まででけた！！
