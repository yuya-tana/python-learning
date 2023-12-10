import requests

url = 'https://book.impress.co.jp/category/program/index_1.php'
res = requests.get(url)
print(res.text)
