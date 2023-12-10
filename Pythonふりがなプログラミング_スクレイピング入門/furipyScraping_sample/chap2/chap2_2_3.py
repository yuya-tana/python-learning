from pathlib import Path
from bs4 import BeautifulSoup

hfile = Path('flowerpark.html')
htext = hfile.read_text(encoding='utf-8')
soup = BeautifulSoup(htext, 'html.parser')
a_tag = soup.find('a')
print(a_tag['href'])
