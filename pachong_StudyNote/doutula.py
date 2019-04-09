import re
from lxml import etree
import requests
import threading
import os
from urllib import request
from queue import Queue

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'

}


# 创建一个线程类，使用生产者消费者模式进行
class Main_thread(threading.Thread):

    # 初始化队列，后面的两个参数加起来代表任意参数
    def __init__(self, spider_queue, img_queue, *args, **kwargs):
        super(Main_thread, self).__init__(*args, **kwargs)
        self.spider_queue = spider_queue
        self.img_queue = img_queue

    def run(self):
        while 1:
            # 如果队列为空，则退出程序
            if self.spider_queue.empty():
                break
            url = self.spider_queue.get()
            self.spider(url)

    def spider(self, url):
        resp = requests.get(url=url, headers=HEADERS)
        text = resp.text
        html = etree.HTML(text)
        imgs = html.xpath('//div[@class="page-content text-center"]//img[@class!="gif"]')
        for img in imgs:
            img_url = img.get('data-original')
            filename = re.sub(r'[，。？！×\*\.]', '', img.get('alt'))
            # 使用os库中的函数获取文件名后缀
            filename = filename + os.path.splitext(img_url)[1]
            # 将图片链接和文件名传入队列当中去
            self.img_queue.put((img_url, filename))


class Cons(threading.Thread):
    def __init__(self, spider_queue, img_queue, *args, **kwargs):
        super(Cons, self).__init__(*args, **kwargs)
        self.spider_queue = spider_queue
        self.img_queue = img_queue

    def run(self):
        while 1:
            if self.spider_queue.empty() and self.img_queue.emtry():
                break
            # 获取文件的下载链接和文件名称
            img_url, filename = self.img_queue.get()
            request.urlretrieve(img_url, './biaoqing_img/' + filename)
            print('=' * 30 + ' 完成下载 ' + filename + '=' * 30)


def main():
    # 初始化队列大小
    spider_queue = Queue(100)
    img_queue = Queue(1000)
    for x in range(80, 101):
        url = 'https://www.doutula.com/photo/list/?page=%s' % x
        spider_queue.put(url)
    # 设置线程数
    for x in range(5):
        t = Main_thread(spider_queue, img_queue)
        t.start()

    for x in range(5):
        t = Cons(spider_queue, img_queue)
        t.start()


if __name__ == '__main__':
    main()
