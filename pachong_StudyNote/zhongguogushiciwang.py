import re
import requests
import threading
import pymongo


def url_parse(url, headers):
    response = requests.get(url=url, headers=headers)
    title = re.findall(r'<div\sclass="cont">.*?<b>(.*?)</b>', response.text, re.DOTALL)
    destory = re.findall(r'<p\sclass="source">.*?<a.*?>(.*?)</a>', response.text, re.DOTALL)
    autor = re.findall(r'<span>：</span><a.*?>(.*?)</a>', response.text, re.DOTALL)
    content_text = re.findall(r'<div class="contson" .*?>(.*?)</div>', response.text, re.DOTALL)
    dianzan_num = re.findall(r'<div class="good"><a.*?><span>&nbsp;(.*?)</span></a>', response.text, re.DOTALL)
    contens = []
    for text in content_text:
        text = re.sub(r'<br.*?>|</?p>', "", text)
        contens.append(text.strip())
    poems = []
    for value in zip(title, destory, autor, content_text, dianzan_num):
        title, destory, autor, content_text, dianzan_num = value
        poem = {
            '诗文标题': title,
            '朝代': destory,
            '作者': autor,
            '正文': contens
        }
        poems.append(poem)

    # 写入文件到txt文件中,
    # for x in poems:
    #     print(x)
    #     with open('./Other/中国古诗文网.txt', 'a+') as f:
    #         f.write(str(x))
    #     f.close()
    # 将结果写入到mongoDB数据库当中去
    client = pymongo.MongoClient('localhost', port=27017)
    db = client.shici
    collection = db.zhongguoshiciwang
    for x in poems:
        print(x)
        collection.insert(x)


def spider():
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36'
    }
    base_url = 'https://www.gushiwen.org/default_{}.aspx'
    for x in range(1, 101):
        url = base_url.format(x)
        print('=' * 40 + '\033[1;31;43m 正在处理第' + str(x) + '页 \033[0m' + '=' * 40)
        url_parse(url, headers)


if __name__ == '__main__':
    try:
        t = threading.Thread(target=spider)
        t.start()
    except Exception as e:
        print(e)
