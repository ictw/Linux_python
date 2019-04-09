# cookie---保存登录状态
from urllib import request, parse


def cookie_easyMethod():
    renrenwang_url = 'http://www.renren.com/880151247/profile'
    hearders = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
        ,
        # 这里的Cookie是响应头中的Cookie.
        'Cookie': 'anonymid=jryom081bwe7hq; depovince=GW; _r01_=1; ick_login=7c632ebc-ca14-428b-905c-f0726a769415; t=c95f0394e1d7e7260b61a40206888b8c6; societyguester=c95f0394e1d7e7260b61a40206888b8c6; id=969691746; xnsid=29598e3f; JSESSIONID=abcdeHsoigjiHbXhNPwJw; ver=7.0; loginfrom=null; jebe_key=b3e14319-aede-4d49-b881-3d963f2c7c42%7Cdd0634284fbb94ffab0504d17e927e5f%7C1549789460020%7C1%7C1549789460029; springskin=set; vip=1; wp_fold=0; jebecookies=0dd87519-3dee-4c76-8ad7-eda2bc85b83d|||||; ch_id=10013; _ga=GA1.2.521749107.1549789474; _gid=GA1.2.47013.1549789474'
    }
    req = request.Request(url=renrenwang_url, headers=hearders)
    resp = request.urlopen(req)
    # print(resp.read().decode("UTF-8"))

    # request.urlretrieve("https:*************/", "./Other/renrenwang_dapeng.html")
    # 两种方法
    with open('./Other/renrenwang_dapeng.html', 'w') as file:
        # resp读取出来的数据是Unicode编码的数据，需要进行转码
        # write()写入数据必须是str类型的
        # bytes-->decode-->str
        file.write(resp.read().decode('UTF-8'))


from http.cookiejar import CookieJar


# url:http://renren.com/
# dapeng_url:http://www.renren.com/880151247/profile
def cookie_Demo():
    # =====创建opener对象=====
    # 创建一个Cookiejar对象
    cookiejar = CookieJar()
    # 使用Cookiejar创建一个HTTPCookieProcess对象
    handler = request.HTTPCookieProcessor(cookiejar)
    # 使用上面创建的handler创建一个opener
    opener = request.build_opener(handler)

    # ==========登录===========
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    data = {
        'email': '15628960878'
        , 'password': 'Renren244'
    }
    login_url = 'http://renren.com/'
    req = request.Request(url=login_url, data=parse.urlencode(data).encode('UTF-8'), headers=headers)
    # 使用opener发送登录请求
    opener.open(req)

    # =========访问===========
    dapeng_url = 'http://www.renren.com/880151247/profile'
    req = request.Request(url=dapeng_url, headers=headers)
    resp = opener.open(req)
    with open('./Other/dapeng_test.html', 'w', encoding='UTF-8') as file:
        file.write(resp.read().decode('UTF-8'))


# cookie_Demo()

from http.cookiejar import MozillaCookieJar


def saveCookie_Demo():
    cookiejar = MozillaCookieJar('./Other/cookie.txt')
    handler = request.HTTPCookieProcessor(cookiejar)
    opener = request.build_opener(handler)

    resp = opener.open('http://httpbin.org/cookies/set?course=suofeiya')
    # 第一个参数代表如果Cookie信息是一种页面响应完立即过期的，则可以将其保存下来
    cookiejar.save(ignore_discard=True)


def loadCookie_Demo():
    cookiejar = MozillaCookieJar('./Other/cookie.txt')
    cookiejar.load(ignore_discard=True)
    for x in cookiejar:
        print(x)


# loadCookie_Demo()

import requests


def cookieByRequest():
    url = 'http://www.renren.com/SysHome.do'
    dapeng_url = 'http://www.renren.com/880151247/profile'
    data = {
        'email': '15628960878'
        , 'password': 'Renren244'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    session = requests.Session()
    session.post(url=url, data=data, headers=headers)
    response = session.get(dapeng_url)
    print(response.text)
    with open('./Other/renren.html', 'w') as file:
        file.write(response.text)


cookieByRequest()
