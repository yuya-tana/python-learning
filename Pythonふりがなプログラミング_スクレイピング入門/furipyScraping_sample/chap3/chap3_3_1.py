import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
news = soup.select_one('div.block-news')
books = news.next_sibling.next_sibling
for h4 in books.select('h4'):
    print(h4.text)
