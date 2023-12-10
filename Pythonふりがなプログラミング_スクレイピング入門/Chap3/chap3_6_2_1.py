import time
import requests
from bs4 import BeautifulSoup

url = 'https://books.rakuten.co.jp/ranking/hourly/001/?l-id=header-subnavi-book-ranking#!/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select('div.item-details > dl > dt > a')

for book in books[:3]:
    book_url = book['href']
    book_res = requests.get(book_url)
    book_soup = BeautifulSoup(book_res.text, 'html.parser')
    book_info = book_soup.select('#productTitle > h1 > a')
    if book_info is None:
        print(book.text, ':要素がありません')
    else:
        print(book.text, ':', book_info.text)
    time.sleep(1)


#item-container > div:nth-child(1) > div.item-details > dl > dt > a
#productTitle > h1 > a

#javascriptを使っているから取得うまいことできないらしい。。？