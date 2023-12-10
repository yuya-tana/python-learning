import unicodedata
from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
ntext = unicodedata.normalize('NFKC', btext)
print(ntext)

# データを扱うとき、表記ゆれがあると読みにくい。そこで、全角アルファベットを半角に、半角カタカナを全角にするプログラム