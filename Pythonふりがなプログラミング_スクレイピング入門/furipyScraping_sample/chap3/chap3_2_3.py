import time
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://book.impress.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
books = soup.select(
    'ol > li > a > '
    'span.module-sub-box-body-img > img')
img_dir = Path('./image')
img_dir.mkdir(exist_ok=True)
for book in books:
    url_rel = book['src']
    url_abs = urljoin(url, url_rel)
    img_res = requests.get(url_abs)
    img_name = Path(url_abs).name
    img_file_path = img_dir / img_name
    img_file_path.write_bytes(img_res.content)
    time.sleep(1)
