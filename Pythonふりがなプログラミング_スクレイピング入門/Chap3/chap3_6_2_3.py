import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.watch.impress.co.jp/category/business/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select('#main > article > section > div > ul > li > div > div.text > p.title > a')

for book in books[:3]:
    book_url = book['href']
    book_res = requests.get(book_url)
    book_soup = BeautifulSoup(book_res.text, 'html.parser')
    book_info = book_soup.select_one('#contents-section-2 > h2 > span')
    if book_info is None:
        print(book.text, ':要素がありません')
    else:
        print(book.text, ':', book_info.text)
    time.sleep(1)



#contents-section-2 > h2 > span
#contents-section-1 > div > div > div > div > span

# ページの中身のタグを取り出すのに使えるコード。ちょっと苦戦した。
    # book_infoのところでまでselectを指定してしまったのが敗因。

