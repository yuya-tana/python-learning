from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://yahoo.co.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select_one(
    'div > div._1UmUawjY6VSzmTK3Y-1sjq > span > picture > img')
url_rel = link['src']
url_abs = urljoin(url, url_rel)
img_res = requests.get(url_abs)
img_name = Path(url_abs).name
img_path = Path(img_name)
img_path.write_bytes(img_res.content)

#tabpanelTopics1 > div > div._3sm0x0pVyxLkf4q9ubmXSL > article > a > div > div._1UmUawjY6VSzmTK3Y-1sjq > span > picture > img
