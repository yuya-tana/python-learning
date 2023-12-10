import time
from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://internetcom.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('ul > li > a > img')

max_scrapes = 5
scrape_count = 0

for link in links:
    if scrape_count >= max_scrapes:
        break

    url_rel = link['src']
    url_abs = urljoin(url, url_rel)
    img_res = requests.get(url_abs)
    # ファイル名から無効な文字を削除または置換
    img_name = Path(url_abs).name
    # safe_img_name = img_name.split('?')[0]  # '?' 以降を削除
    # 画像ファイルを保存
    img_path = Path(img_name)
    img_path.write_bytes(img_res.content)

    scrape_count += 1
    time.sleep(1)


# うまく実行できるサイト探すのだけでも一苦労だ。。
