import requests
from bs4 import BeautifulSoup

url = 'https://internetcom.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select_one('div.maker-child').parent
print(link['class'])