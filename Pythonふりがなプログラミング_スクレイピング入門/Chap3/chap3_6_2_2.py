import time
import requests
from bs4 import BeautifulSoup

url = 'https://www.e-hon.ne.jp/bec/EB/Top'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select('#ranking-001 > ol > div > div > li > span.text > span.title > a')

for book in books[:3]:
    book_url = book['href']
    book_res = requests.get(book_url)
    book_soup = BeautifulSoup(book_res.text, 'html.parser')
    book_info = book_soup.select('#main > div.commentContents > div > section > div > p')
    if book_info is None:
        print(book.text, ':要素がありません')
    else:
        print(book.text, ':', book_info.text)
    time.sleep(1)


#item-container > div:nth-child(1) > div.item-details > dl > dt > a
#productTitle > h1 > a

#javascriptを使っているから取得うまいことできないらしい。。？

#ranking-001 > ol > div > div > li.rank1.m-common_item.slide-item.slick-slide.slick-current.slick-active > span.thumb > a > img
#ranking-001 > ol > div > div > li.rank1.m-common_item.slide-item.slick-slide.slick-current.slick-active > span.text > span.title > a
#ranking-001 > ol > div > div > li.rank2.m-common_item.slide-item.slick-slide.slick-active > span.text > span.title > a
#main > div.commentContents > div > section > div > p:nth-child(2)