from pathlib import Path
import requests

url = ('https://www.googleapis.com/books/v1/'
       'volumes?q=+intitle:ふりがな'
       '+inpublisher:インプレス')
res = requests.get(url)
bjson = Path('books.json')
bjson.write_text(res.text, encoding='utf-8')
