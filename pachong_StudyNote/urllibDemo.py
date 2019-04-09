from urllib import request
from urllib import parse


def urlopenDemo():
    # urlopen简单使用，请求一个url,属于request
    resp = request.urlopen("https://www.bilibili.com/")
    print(resp.read())


def urlretrieveDemo():
    # urlretrieve可以把网页上的一个文件保存到本地，属于request
    request.urlretrieve("https://www.bilibili.com/", "./Other/bilibili.html")


def urlencodeDemo():
    # urlencode函数用于编码，属于parse
    # params = {'name': 'suofeiya', 'age': 21, 'Python': 'hello world'}
    # print(parse.urlencode(params))
    url = 'http://www.baidu.com/'
    params = {'wd': '索菲娅'}
    ps = parse.urlencode(params)
    url = url + "s?" + ps
    print(url)
    resp = request.urlopen(url)
    print(resp.read())


def parse_qsDemo():
    # 解码，与上面相反
    params = {"wd": "%E7%B4%A2%E8%8F%B2%E5%A8%85"}
    print(parse.parse_qs(params))


def urlparseDemo():
    # 分部分提取，属于parse
    url = 'https://www.baidu.com/s;hello world?wd=%E7%B4%A2%E8%8F%B2%E5%A8%85&pn=60&oq=%E7%B4%A2%E8%8F%B2%E5%A8%85&ie=utf-8&usm=2&rsv_idx=1&rsv_pq=de6a66bb000adffa&rsv_t=ef72MdHnSqAuC9c7DVjH7siSkhNhlFN0LXjiV2dQlvMq3ZqpOAbM%2Fxh8vNk'
    result = parse.urlparse(url)
    print("scheme:", result.scheme)
    print("netloc:", result.netloc)
    print("path:", result.path)
    print("query:", result.query)
    print(result)
    print("==================")
    # 区别在于后者urlsplit()，没有params参数
    print(parse.urlsplit(url))


def requestDemo():
    # 设置请求头
    # url = 'http://www.lagou.com/zhaopin/Java/?labelWords=label'
    url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
    data = {
        'first': 'true',
        'pn': 1,
        'kd': 'python'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        , 'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput='
        # , 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
        # , 'Accept': ' application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': ' gzip, deflate, br',
        # 'Accept-Language': ' zh-CN,zh;q=0.9',
        # 'Connection': ' keep-alive',
        # 'Content-Length': ' 25'
        # ,'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
    }
    # encode()将其编码成UTF-8
    # url，请求头，请求的数据，方式
    req = request.Request(url=url, headers=headers, data=parse.urlencode(data).encode('UTF-8'), method='POST')
    resp = request.urlopen(req)
    # 将输出结果解码成UTF-8，不然显示不正常
    print(resp.read().decode('UTF-8'))


# requestDemo()
urlopenDemo()