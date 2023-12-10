import requests
from bs4 import BeautifulSoup

url = 'https://yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
list = soup.select_one(
    'ul > li:nth-child(2) > div > a'
)
print(list)
print(list.text)



#ToolList > ul > li:nth-child(1) > div > a