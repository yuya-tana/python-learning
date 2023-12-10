from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
book = soup.select_one(
    'ol > li.moduke-rank-01 > a > '
    'span.module-sub-box-body-img > img')
url_rel = book['src']
url_abs = urljoin(url, url_rel)
img_res = requests.get(url_abs)
img_name = Path(url_abs).name
img_path = Path(img_name)
img_path.write_bytes(img_res.content)
