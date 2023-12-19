from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
jtext = btext.replace('第1位','第1位:')
print(jtext)