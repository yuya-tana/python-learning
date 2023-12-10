import requests

url = 'https://yahoo.co.jp/'
res = requests.get(url)
print(res.text[:500])

# 書籍内ではbook.impress.co.jp指定していたものの、SSLの関係で取得できたなかったため一旦yahooへ