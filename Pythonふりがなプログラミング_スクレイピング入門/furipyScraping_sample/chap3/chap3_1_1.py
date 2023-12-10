from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select(
    'div.block-sub-box-body > ol > li > a')
for book in books:
    book_name = book.get_text(strip=True)
    book_url = urljoin(url, book['href'])
    print(book_name)
    print(book_url)
