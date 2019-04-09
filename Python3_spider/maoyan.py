import json
import re
import time
import requests
from requests import RequestException


def get_html(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36'
        }
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            return resp.text
        return None
    except RequestException:
        return None


def get_details(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
        + '.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
        + '.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>',
        re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '索引': item[0],
            '电影名称': item[1],
            '海报链接': item[2].strip(),
            '主演': item[3].strip(),
            '上映时间及地区': item[4].strip(),
            '评分': item[5] + item[6]
        }


def write2json(content):
    with open('./Other/maoyan_top100.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + ',\n')


def main(offset):
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_html(url)
    for item in get_details(html):
        print(item)
        write2json(item)


if __name__ == '__main__':
    for x in range(10):
        main(offset=x * 10)
        time.sleep(1)
