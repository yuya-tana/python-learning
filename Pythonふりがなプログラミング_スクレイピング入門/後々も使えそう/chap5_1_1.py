from pathlib import Path
import requests

url =('https://www.googleapis.com/books/v1/volumes?q=+intitle:ふりがな+inpublisher:インプレス')
res = requests.get(url)
bjson = Path('books.json')
bjson.write_text(res.text, encoding='utf-8')

# 書名がふりがな、発行元がインプレスの書籍情報を取り出し結果をファイルに保存する