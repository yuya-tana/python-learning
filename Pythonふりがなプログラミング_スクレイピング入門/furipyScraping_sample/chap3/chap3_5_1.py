import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.j'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find('h2').text)
