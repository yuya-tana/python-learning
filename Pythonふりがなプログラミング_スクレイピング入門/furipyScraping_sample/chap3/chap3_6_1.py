import sys
import requests
from bs4 import BeautifulSoup

url = ('https://book.impress.co.jp/category/'
       'program/index_1.php')
res = requests.get(url)
if res.status_code != requests.codes.ok:
    print('Error! status_code is ：',
          res.status_code)
    sys.exit(1)
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.find('a'))
