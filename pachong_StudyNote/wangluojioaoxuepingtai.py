"""
辣鸡网络教学平台《组件式GIS》爬虫练习_regular
"""
import requests
import re
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Mobile Safari/537.36',
    # 'Cookie': 'JSESSIONID=73D10635E159E450AB380E50901C1493',
    'Referer': 'http://211.64.127.164/meol/common/script/listview.jsp?acttype=enter&folderid=219532&lid=23324'

}


def savefiles(url):
    try:
        r = requests.get(url, headers=headers)
        # filename = time.asctime(time.localtime(time.time()))
        filename = re.findall('(\r\n)*<p>文件名:<span>(.*?)</span>', r.text, re.DOTALL)
        print(url)
        # for x in filename:
        #     print(x)
        # with open('./download/' + filename, "wb") as code:
        #     print("=" * 30 + "正在下载”" + filename + "“" + "=" * 30)
        #     code.write(r.content)
    except Exception as e:
        print(e)


def download(url):
    download_urls = requests.get(url=url, headers=headers)
    urls = re.findall('(\r\n)*<a class="icon32 lv-download" href="(.*?)".*?>', download_urls.text, re.DOTALL)
    for x in urls:
        savefiles("http://211.64.127.164/" + x[1])


def parseDetailUrl(detail_url):
    try:
        detail_urls = requests.get(url=detail_url, headers=headers)
        urls = re.findall('(\r\n)*<a href="(pre.*?)"', detail_urls.text, re.DOTALL)
        for x in urls:
            download("http://211.64.127.164/meol/common/script/" + x[1])
    except Exception as e:
        print(e)


def parseDownloadUrl(url, headers):
    base_url = requests.get(url=url, headers=headers)
    tbody_urls = re.findall('(\r\n)*<a href="(list.*?)"', base_url.text, re.DOTALL)
    for x in tbody_urls:
        parseDetailUrl(detail_url="http://211.64.127.164/meol/common/script/" + str(x[1]))


def spider():
    url = 'http://211.64.127.164/meol/common/script/listview.jsp?acttype=enter&folderid=219532&lid=23324'
    parseDownloadUrl(url, headers)


if __name__ == '__main__':
    spider()
