import re
from pathlib import Path
from bs4 import BeautifulSoup

hfile = Path('flowerpark.html')
htext = hfile.read_text(encoding='utf-8')
soup = BeautifulSoup(htext, 'html.parser')
pattern = re.compile('h[1-4]')
for h_tag in soup.find_all(pattern):
    print(h_tag)



# re.compile(正規表現)　を扱うためのモジュール