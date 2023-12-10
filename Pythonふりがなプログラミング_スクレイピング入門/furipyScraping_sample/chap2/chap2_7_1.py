import requests

url = 'https://book.impress.co.jp/'
res = requests.get(url)
print(res.text[:1000])
