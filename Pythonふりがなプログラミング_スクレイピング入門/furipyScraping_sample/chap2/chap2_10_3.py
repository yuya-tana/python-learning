from pathlib import Path
import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select(
    'ol > li > a > span.module-sub-box-body-txt')
btext = ''
for book in books:
    btext += book.text
    btext += '\n'
efile = Path('top5books.txt')
efile.write_text(btext, encoding='utf-8')
