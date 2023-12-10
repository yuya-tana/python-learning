from pathlib import Path
from bs4 import BeautifulSoup

hfile = Path('flowerpark.html')
htext = hfile.read_text(encoding='utf-8')
soup = BeautifulSoup(htext, 'html.parser')
for news in soup.find_all(class_='block-news'):
    print(news.find('h2'))
