import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
book = soup.select_one(
    'ol > li.moduke-rank-01 > a > '
    'span.module-sub-box-body-txt')
print(book)
print(book.text)
