import re
from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
stext = re.sub(r'(第[1-3]位)', r'\1：', btext)
print(stext)
