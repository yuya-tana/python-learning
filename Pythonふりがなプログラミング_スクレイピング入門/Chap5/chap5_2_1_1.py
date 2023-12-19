import time
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from bs4 import BeautifulSoup

# Service オブジェクトの作成
service = Service(executable_path=binary_path)

# Service オブジェクトを使用して Chrome を初期化
with Chrome(service=service) as driver:
    driver.get('https://www.watch.impress.co.jp/')
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.select('#allsite-access-ranking-ul-latest > li')
    for article in articles:
        print(article.text)


# テストで使っているこのサイトだと、証明書の問題で変なエラーが出るものの、サイトを閉じる際には問題なく取得したい結果が取得できていそう。