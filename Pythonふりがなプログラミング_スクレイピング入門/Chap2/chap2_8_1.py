from  pathlib import Path
import requests

url = 'https://yahoo.co.jp/'
res = requests.get(url)
rfile = Path('response.txt')
rfile.write_text(res.text, encoding='utf-8')