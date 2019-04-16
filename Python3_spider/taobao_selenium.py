import pymongo
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pyquery import PyQuery as pq
from urllib.parse import quote

from Linux_python.Python3_spider.taobao_config import *

browser = webdriver.Chrome(executable_path=r'/home/suofeiya/pycharm-2019.1.1/bin/chromedriver')

wait = WebDriverWait(browser, 10)
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]


def login():
    login_url = "https://login.taobao.com/member/login.jhtml"
    browser.get(login_url)
    print('Scan the QRcode or input your login information to login(IN 60s)')
    try:
        WebDriverWait(browser, 60).until(
            EC.url_changes
        )
        browser.implicitly_wait(2)
    except TimeoutException:
        print("Time out!")


def get_index(page):
    print("Spidering page " + str(page))
    try:
        url = "https://s.taobao.com/search?q=" + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page))
        )
        wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item'))
        )
        get_infos()
    except TimeoutException:
        get_index(page)


def get_infos():
    html = browser.page_source
    doc = pq(html)
    items = doc('#mainsrp-itemlist .items .item J_MouserOnverReq  ').items()
    for item in items:
        product = {
            'image': item.find('.pic .img').attr('data-src'),
            'price': item.find('.price').text(),
            'deal': item.find('.deal-cnt').text(),
            'title': item.find('.title').text(),
            'shop': item.find('.shop').text(),
            'location': item.find('.location').text()
        }
        print(product)
        save2Mongo(product)


def save2Mongo(result):
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('save to mongoDB successfully')
    except Exception:
        print('save to mongoDB ERROR')


def main():
    login()
    for x in range(1, MAX_PAGE + 1):
        get_index(x)
    browser.close()


if __name__ == '__main__':
    main()
