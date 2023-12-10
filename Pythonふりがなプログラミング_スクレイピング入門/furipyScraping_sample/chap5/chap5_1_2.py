import json
from pathlib import Path

bjson = Path('books.json')
bjson_text = bjson.read_text(encoding='utf-8')
bjson_dic = json.loads(bjson_text)
for item in bjson_dic['items']:
    print(item['volumeInfo']['title'])
