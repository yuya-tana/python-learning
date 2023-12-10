import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
for h2 in soup.find_all('h2'):
    print(h2)
