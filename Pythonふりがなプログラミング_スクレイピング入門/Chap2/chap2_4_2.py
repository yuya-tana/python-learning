from pathlib import Path
from bs4 import BeautifulSoup

hfile = Path('flowerpark.html')
htext = hfile.read_text(encoding='utf-8')
soup = BeautifulSoup(htext, 'html.parser')
for h_tag in soup.find_all(['h1', 'h2', 'h3']):
    print(h_tag)