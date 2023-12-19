from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
jtext = btext.title()
print(jtext)