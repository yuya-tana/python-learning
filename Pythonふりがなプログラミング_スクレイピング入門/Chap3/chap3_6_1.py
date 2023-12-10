import sys
import requests
from bs4 import BeautifulSoup

url = 'http://example.invalid/'
res = requests.get(url)
if res.status_code != requests.codes.ok:
    print('Error! status_code is :', res.status_code)
    sys.exit(1)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find('a'))

# 存在しないサイトを指定したものの、powershell側でエラーを吐いてしまい、定義している部分のエラーまではたどり着かず、、リンク切れになってるサイトとか指定出来ればいけそうな予感。