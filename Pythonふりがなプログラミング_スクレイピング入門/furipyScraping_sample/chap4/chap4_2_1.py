import unicodedata
from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
ntext = unicodedata.normalize('NFKC', btext)
print(ntext)
