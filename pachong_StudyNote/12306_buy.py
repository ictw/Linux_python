import base64
import re
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Qiangpiao(object):

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'/home/suofeiya/pycharm-2018.3.5/chromedriver')
        self.login_url = 'https://kyfw.12306.cn/otn/login/init'
        self.after_login_url = 'https://kyfw.12306.cn/otn/view/index.html'
        self.passwd = base64.b64decode('ZGFpbWluZ3lvbmcyNDQ=\n')
        self.search_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc'
        self.buy_ticket_url = 'https://kyfw.12306.cn/otn/confirmPassenger/initDc'
        # 输入购票信息
        self.from_station = input('请输入您的起始车站：')
        self.to_station = input('请输入您的目的地：')
        self.start_time = input('请输入出发时间（yyyy-mm-dd）：')
        self.passagers = input('乘客姓名（多个乘客用英文逗号隔开）：').split(',')
        self.trans = input('请输入您的车次信息（多个车次使用英文逗号分离）').split(',')

    def _login(self):
        self.driver.get(self.login_url)
        self.driver.find_element_by_id('username').send_keys('daimingyong266')
        self.driver.find_element_by_id('password').click()
        self.passwd = re.sub('\'|b', '', str(self.passwd))
        self.driver.find_element_by_id('password').send_keys(self.passwd)
        # noinspection PyBroadException
        try:
            WebDriverWait(self.driver, 60).until(
                EC.url_to_be(self.after_login_url)
            )
            # self.driver.execute_script('alert(">>>>登陆成功，请停止您当前的操作<<<<")')
            print('>' * 40 + '登陆成功！' + '<' * 40)
        except Exception:
            print('异常终止.')
            sys.exit()

    def _order_ticket(self):
        self.driver.get(self.search_url)

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'fromStationText'), self.from_station)
        )

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'toStationText'), self.to_station)
        )

        WebDriverWait(self.driver, 1000).until(
            EC.text_to_be_present_in_element_value((By.ID, 'train_date'), self.start_time)
        )
        # 如果能够被点击
        WebDriverWait(self.driver, 1000).until(
            EC.element_to_be_clickable((By.ID, 'query_ticket'))
        )

        submitBtn = self.driver.find_element_by_id('query_ticket')
        submitBtn.click()

        WebDriverWait(self.driver, 1000).until(
            EC.presence_of_element_located((By.XPATH, './/tbody[@id="queryLeftTable"]/tr'))
        )

        # 寻找所有不是tr属性为datatran的元素
        trs = self.driver.find_elements_by_xpath('.//tbody[@id="queryLeftTable"]/tr[not(@datatran)]')
        for tr in trs:
            train_number = tr.find_element_by_class_name('number').text
            if train_number in self.trans:
                left_ticket = tr.find_element_by_xpath('.//td[last()-2]').text
                if left_ticket == '有' or left_ticket.isdigit:
                    print('当前车次' + train_number + '有票')
                    orderBtn = tr.find_element_by_class_name('btn72')
                    orderBtn.click()

                    WebDriverWait(self.driver, 1000).until(
                        EC.url_to_be(self.buy_ticket_url)
                    )
                    self.driver.get(self.buy_ticket_url)
                    passenger_ids = self.driver.find_elements_by_xpath('//ul[@id="normal_passenger_id"]')
                    for ids in passenger_ids:
                        id = ids.find_element_by_xpath('.//label').text
                        print(id)

                else:
                    print('当前车次' + train_number + '无票')

    def run(self):
        self._login()
        self._order_ticket()


if __name__ == '__main__':
    spider = Qiangpiao()
    spider.run()
