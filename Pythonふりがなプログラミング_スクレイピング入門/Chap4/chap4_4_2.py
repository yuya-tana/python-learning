import re
from pathlib import Path

bpath = Path('book.txt')
btext = bpath.read_text(encoding='utf-8')
jtext = re.sub(r'(第[1-3]位)', r'\1:', btext)
print(jtext)


# 正規表現で置き換えを行う箇所のかっこをきちんとつけてあげる必要がある。