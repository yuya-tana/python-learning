from pathlib import Path
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

url = 'https://tver.jp/series/sr9gfdf2ex/'
res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')
link = soup.select_one('div > div > img')
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

# <span class="rStpk9W4eUO5IMVhnJylj _9lUaMh5eQv_w-n4J18isw">
# <img src="https://quriosity-pctr.c.yimg.jp/G6mIQ2g9ovT9ordcB91SvIa7qrC4bJ70ftaInRROR7bWB84Y3jNE6cJhPKYzTRuRkGFeo1Qh4D0SGk9vHyo0tk5Jjz3ZniLo-zCO0KIpehSThya7aohHm3dZsIpWvJlRIbcE8Hg9g5BtpGqI4lZhRW-_l8bHChkDCo2pW8FcWrQ=" width="80" height="80" alt="" loading="lazy"></span>

# jin #contents > div.autopagerize_page_element > section:nth-child(2) > div > div.index_article_body > a > p > img SSLでだめ。

#body > main > div.l-contents.top-arrival.js-top-arrival.m-article.--col4 > article:nth-child(1) > a > div.m-article-item-imgwrap > img

#__next > main > div > div > div.series-page-main_seriesContent___SMYI > div > div.episode-live-list-column_season__F5sjW > div > div:nth-child(1) > a > div.episode-row_thumbnail__xAGyA > div.episode-row_imgWrapper__iOG2W.thumbnail-img_wrapper__nn7Tb.thumbnail-img_ratio169__Lw3xS > img