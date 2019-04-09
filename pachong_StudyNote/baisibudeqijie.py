import requests
from lxml import etree
import re
from urllib import request
import threading
from queue import Queue


class MainThread(threading.Thread):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'
    }

    def __init__(self, spider_queue, mp3_queue, *args, **kwargs):
        super(MainThread, self).__init__(*args, **kwargs)
        self.spider_queue = spider_queue
        self.mp3_queue = mp3_queue

    def run(self):
        while True:
            if self.spider_queue.empty():
                break
            url = self.spider_queue.get()
            self.spider(url)

    def spider(self, url):
        resp = requests.get(url, headers=self.headers)
        text = resp.text
        html = etree.HTML(text)
        titles = html.xpath(
            '//div[@class="j-r-list-tool-r j-r-list-tool-cc"]//li[@class="j-r-list-tool-l-down f-tar j-down-video j-down-hide ipad-hide"]')
        mp3_urls = html.xpath(
            '//div[@class="j-r-list-tool-r j-r-list-tool-cc"]//li[@class!=" f-tac j-comment j-comment-width  j-comment-down-width"]//a')
        for x in titles:
            haibao_url = x.get('data-pic')
            for y in mp3_urls:
                mp3_url = y.get('href')
            filename = x.get('data-text')
            filename = re.sub(r'[，。#？！×\?\*\. ]', '', filename.strip())
            self.mp3_queue.put((filename, haibao_url, mp3_url))


class Cons(threading.Thread):

    def __init__(self, spider_queue, mp3_queue, *args, **kwargs):
        super(Cons, self).__init__(*args, **kwargs)
        self.spider_queue = spider_queue
        self.mp3_queue = mp3_queue

    def run(self):
        while True:
            if self.spider_queue.empty() and self.mp3_queue.empty():
                break
            filename, haibao_url, mp3_url = self.mp3_queue.get()
            request.urlretrieve(haibao_url, './baisibudejie/' + filename + '.jpg')
            print('=' * 10 + "完成名称为" + filename + '.jpg' + '海报的的下载' + '=' * 10)
            request.urlretrieve(mp3_url, './baisibudejie/' + filename + '.mp3')
            print('=' * 10 + "完成名称为" + filename + '.mp3' + '歌曲的下载' + '=' * 10)


def main():
    spider_queue = Queue(100)
    mp3_queue = Queue(1000)
    for x in range(1, 101):
        url = 'http://www.budejie.com/audio/%s' % x
        spider_queue.put(url)

    for x in range(10):
        t = MainThread(spider_queue, mp3_queue)
        t.start()

    for x in range(10):
        t = Cons(spider_queue, mp3_queue)
        t.start()


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
