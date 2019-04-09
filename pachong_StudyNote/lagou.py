import re
import time

import pymongo
from selenium import webdriver
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Lagou_spider(object):
    driver_path = r'/home/suofeiya/pycharm-2018.3.5/chromedriver'

    def __init__(self):
        # 初始化浏览器的设置
        self.driver = webdriver.Chrome(executable_path=Lagou_spider.driver_path)
        self.url = 'https://www.lagou.com/jobs/list_java?labelWords=&fromSearch=true&suginput=?labelWords=hot'
        # 新建一个列表来保存信息
        self.lagou_webpage = []

    def run(self):
        # 获取主页url中的内容
        self.driver.get(self.url)
        # 设置循环以取得所有ajax的数据
        while 1:
            # 设置延时
            WebDriverWait(driver=self.driver, timeout=10).until(
                EC.presence_of_element_located((By.XPATH, '//div[@class="pager_container"]/span[last()]'))
            )

            source = self.driver.page_source

            self.get_detail_urls(source)

            next_btn = self.driver.find_element_by_xpath('//div[@class="pager_container"]/span[last()]')
            if 'pager_next pager_next_disabled' in next_btn.get_attribute('class'):
                break
            else:
                next_btn.click()

    def get_detail_urls(self, source):
        html = etree.HTML(source)
        detail_urls = html.xpath('//a[@class="position_link"]/@href')
        for detail_url in detail_urls:
            self.get_detail_info(detail_url)
            time.sleep(1)

    def get_detail_info(self, detail_url):

        # self.driver.get(url)
        self.driver.execute_script('window.open("%s")' % detail_url)
        self.driver.switch_to.window(self.driver.window_handles[1])

        WebDriverWait(driver=self.driver, timeout=10).until(
            EC.presence_of_element_located((By.XPATH, '//dd[@class="job_bt"]'))
        )

        source = self.driver.page_source
        self.get_info(source)
        # 关闭当前标签
        self.driver.close()
        # 跳转到第一个标签
        self.driver.switch_to.window(self.driver.window_handles[0])

    def get_info(self, source):
        html = etree.HTML(source)
        company_name = html.xpath('//div[@class="company"]/text()')[0]
        job_name = html.xpath('//span[@class="name"]/text()')[0]
        job_request = html.xpath('//dd[@class="job_request"]//span')
        salary = html.xpath('//span[@class="salary"]/text()')[0].strip()
        city = job_request[1].xpath('.//text()')[0].strip()
        city = re.sub(r'[\s/]', '', city)
        work_years = job_request[2].xpath('.//text()')[0].strip()
        work_years = re.sub(r'[\s/]', '', work_years)
        education = job_request[3].xpath('.//text()')[0].strip()
        education = re.sub(r'[\s/]', '', education)
        job_type = job_request[4].xpath('.//text()')[0].strip()
        job_advantage = html.xpath('//dd[@class="job-advantage"]//p/text()')[0]
        job_detail = ''.join(html.xpath('//dd[@class="job_bt"]//text()')).strip()
        work_address = ''.join(html.xpath('//div[@class="work_addr"]//text()')).strip()
        work_address = re.sub('[\s]|\\n|查看地图', '', work_address)
        lagou = {
            '公司名称': company_name,
            '工作名称': job_name,
            '薪水': salary,
            '公司地点': city,
            '工作年限': work_years,
            '工作地址': work_address,
            '要求': education,
            '工作性质': job_type,
            '工作优点': job_advantage,
            '详细信息': job_detail
        }
        self.lagou_webpage.append(lagou)
        print(Lagou_spider)
    #     self.write2mongoDB(self.lagou_webpage)
    #
    # def write2mongoDB(self):
    #     # 写入mongoDB
    #
    #     client = pymongo.MongoClient('localhost', port=27017)
    #     db = client.lagou
    #     collection = db.lagou_spider
    #     collection.insert(self.lagou_webpage)
    #

if __name__ == '__main__':
    spider = Lagou_spider()
    spider.run()
