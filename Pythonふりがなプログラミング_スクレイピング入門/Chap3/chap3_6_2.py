import time
import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/category/soft/pcguide/index.php'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select('div.module-book-list-item-body-head > h4 > a')

for book in books[:3]:
    book_url = book['href']
    book_res = requests.get(book_url)
    book_soup = BeautifulSoup(book_res.text, 'html.parser')
    book_info = book_soup.select('div.module-book-copy > h3')
    if book_info is None:
        print(book.text, ':要素がありません')
    else:
        print(book.text, ':', book_info.text)
    time.sleep(1)


#body > div.block-wrap > div.block-content > main > div > div.block-book-list.module-img-s > div.block-book-list-body > div:nth-child(1) > div > div > div:nth-child(3) > div.module-book-list-item-body > div.module-book-list-item-body-head > h4 > a
#body > div.block-wrap > div.block-content > main > div > div.block-book-detail > div.block-book-detail-body > div.module-book-detail-txt > div.module-book-copy > h3