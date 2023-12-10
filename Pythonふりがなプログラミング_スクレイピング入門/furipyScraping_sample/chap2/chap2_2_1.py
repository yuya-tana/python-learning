from pathlib import Path

hfile = Path('flowerpark.html')
htext = hfile.read_text(encoding='utf-8')
print(htext[:150])
