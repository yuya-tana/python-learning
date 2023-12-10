from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
rtext = btext.replace('第1位', '第1位：')
print(rtext)
