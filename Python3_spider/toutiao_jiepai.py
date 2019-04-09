import os
import re
from hashlib import md5
from multiprocessing.pool import Pool

import requests
from urllib.parse import urlencode

from requests import codes


def get_page(offset):
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        # 'keyword': '街拍',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
        'pd': 'synthesis',
        # 'timestamp': timestamp
    }
    # 使用urlencode将param参数转换为url形式
    url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D' + urlencode(params)
    try:
        resp = requests.get(url)
        print(url)
        if resp.status_code == codes.ok:
            # 返回数据类型为json类型
            return resp.json()
    except requests.ConnectionError:
        return None


def get_images(json):
    if json.get('data'):
        data = json.get('data')
        for item in data:
            # 观察json数据可得知当data中无cell_type时，数据才是正确的
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                # 该正则表达意思为：将url中的list全部天幻为origin
                origin_image = re.sub("list", "origin", image.get('url'))
                yield {
                    'image_url': origin_image,
                    'title': title
                }


def save_images(item):
    # 设置image放置所在目录位置，第二个代表斜线/
    img_path = 'img' + os.path.sep + item.get('title')
    # 如果该目录不存在，则创建
    if not os.path.exists(img_path):
        # 使用os.makedirs来进行递归创建文件夹
        os.makedirs(img_path)
    try:
        resp = requests.get(item.get('image_url'))
        if resp.status_code == codes.ok:
            # image写入地址，使用文件的md5值用来作为文件名，保证不会下载到重复的文件
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(resp.content).hexdigest(),
                file_suffix='jpg')
            # 如若文件不存在
            if not os.path.exists(file_path):
                # 则以二进制格式写入
                with open(file_path, 'wb') as fb:
                    fb.write(resp.content)
                print('下载文件地址为： %s' % file_path)
            else:
                print('该文件已下载', file_path)
    except requests.ConnectionError():
        print('尝试保存images出错')


def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_images(item)


GROUP_START = 0
GROUP_END = 8
if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
