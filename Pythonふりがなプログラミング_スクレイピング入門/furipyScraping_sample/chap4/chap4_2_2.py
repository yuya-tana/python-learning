import jaconv
from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
jtext = jaconv.h2z(btext, kana=True,
                   digit=True, ascii=True)
print(jtext)
