import time
from selenium.webdriver import Chrome
from chromedriver_py import binary_path
from bs4 import BeautifulSoup

with Chrome(executable_path=binary_path) as driver:
    driver.get('https://www.watch.impress.co.jp/')
    time.sleep(5)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    articles = soup.select('#allsite-access-ranking-ul-latest > li')
    for article in articles:
        print(article.text)
