import requests
from bs4 import BeautifulSoup

url = 'https://yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
lists = soup.select(
    '#ToolList > ul > li > div > a '
)
for list in lists:
    print(list.text)



#ToolList > ul > li:nth-child(1) > div > a
#> li:nth-of-type(1) > div > a