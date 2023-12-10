import requests
from bs4 import BeautifulSoup

url = 'https://yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
for h1 in soup.find_all('h1'):
    print(h1)

# 書籍内ではbook.impress.co.jp指定していたものの、SSLの関係で取得できたなかったため一旦yahooへ