import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select('ol > li > a > span.module-sub-box-body-txt')
print(books.text)
