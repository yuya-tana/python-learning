from pathlib import Path
import requests

url = 'https://book.impress.co.jp/'
res = requests.get(url)
rfile = Path('response.txt')
rfile.write_text(res.text, encoding='utf-8')
