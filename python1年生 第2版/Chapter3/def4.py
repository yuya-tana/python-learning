import random
def omikuji():
    kuji = ['大吉','中吉','吉','凶',]
    return random.choice(kuji)
kekka = omikuji()
print("結果は",kekka,"です。")

# 戻り値だけがある関数。ランダムで出力されるものの戻り値だけをしっかりreturnでとらえてプリントする