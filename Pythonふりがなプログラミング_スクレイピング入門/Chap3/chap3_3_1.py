import requests
from bs4 import BeautifulSoup

url = 'https://internetcom.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select_one('#contents')
i = link.next_sibling.next_sibling
for h4 in i.select('li.copyright'):
    print(h4.text)


#contents > div:nth-child(3) > div > div:nth-child(1) > a > div.center-wrap > img
#contents > div:nth-child(3) > div > div:nth-child(1) > a > div:nth-child(2)   ul > li > a > img

# 例みたいに良い感じにh4タグとか指定しているのがなかったので、liのclassとしてcopyright使っているものを指定してみた。