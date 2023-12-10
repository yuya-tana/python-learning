from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://internetcom.jp/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select_one('ul > li > a > img')
url_rel = link['src']
url_abs = urljoin(url, url_rel)
img_res = requests.get(url_abs)

# ファイル名から無効な文字を削除または置換
img_name = Path(url_abs).name
safe_img_name = img_name.split('?')[0]  # '?' 以降を削除

# 画像ファイルを保存
img_path = Path(safe_img_name)
img_path.write_bytes(img_res.content)

#tabpanelTopics1 > div > div._3sm0x0pVyxLkf4q9ubmXSL > article > a > div > div._1UmUawjY6VSzmTK3Y-1sjq > span > picture > img


# yahooの画像の命名規則？(クエリルール)によって「?」が画像の名前に入ってしまっていたので、それを取り除く処理を追加したらきちんと画像保存が行えた


# #qurireco > article:nth-child(1) > a > div > div._7uaWVw_YSgf_GKoctUM12 > span > img
#contents > div:nth-child(4) > div.span8 > ul:nth-child(3) > li:nth-child(2) > a > img