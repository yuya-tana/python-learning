import re
from pathlib import Path
from bs4 import BeautifulSoup

hfile = Path('flowerpark.html')
htext = hfile.read_text(encoding='utf-8')
soup = BeautifulSoup(htext, 'html.parser')
pattern = re.compile('フラワー|Flower|flower')
for h2 in soup.find_all('h2', string=pattern):
    print(h2)
