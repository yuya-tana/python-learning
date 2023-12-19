from pathlib import Path
import json

bjson = Path('books.json')
bjson_text = bjson.read_text(encoding='utf-8')
bjson_dic = json.loads(bjson_text)
for item in bjson_dic['items']:
    print(item['volumeInfo']['title'])

# books.jsonを確認すると、itemsキー内の要素0~がそれぞれ書籍情報となっているので、その辺りを指定することで書籍が抜き出せる
    #printでitemのvolumeInfoの中からtitleを抜き出すように指示をしている形。
    #WebAPIによってJsonの出力が異なるので、色々確認する必要はあるが、基本を押さえれば応用ができる！！