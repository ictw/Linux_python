import requests
from urllib.parse import quote

# render.html的详细api参数在https://splash.readthedocs.io/en/stable/api.html#render.html
def easyDemo():
    # render接口基本用法
    url = 'http://0.0.0.0:8050/render.html?url=https://www.baidu.com'
    resp = requests.get(url)
    print(resp.text)


def demo1():
    # 获取页面截图，类似还有render.jpeg，外加参数有图片质量.
    url = 'http://0.0.0.0:8050/render.png?url=https://www.jd.com&wait=3&width=1000&height=700'
    resp = requests.get(url)
    with open('./Other/jingdong.png', 'wb') as f:
        f.write(resp.content)
    print("截图已保存")


def demo2():
    # 获取页面的HAR数据，类型为JSON
    # 直接在terminal中执行curl [url]同样的效果
    url = 'http://0.0.0.0:8050/render.har?url=https://www.jd.com&wait=3'
    resp = requests.get(url)
    print(resp.json())


def demo3():
    url = 'http://0.0.0.0:8050/render.json?url=https://httpbin.org'
    resp = requests.get(url)
    print(resp.text)


def executeDemo():
    # lua = """
    # function main(splash)
    #     return 'suofeiya'
    # end
    # """
    # print(quote(lua))
    # url = 'http://0.0.0.0:8050/execute?lua_source=' + quote(lua)
    # resp = requests.get(url)
    # print(resp.text)
    lua = """
    function main(splash,args)
        local treat = require('treat')
        local resp=splash:http_get('http://httpbin.org/get')
            return{
                html = treat.as_string(resp.body),
                url  = resp.url,
                status = resp.status
            }
    end
    """
    # 注意此处splash API 中的execute的写法
    url = 'http://0.0.0.0:8050/execute?lua_source=' + quote(lua)
    resp = requests.get(url)
    print(resp.text)


if __name__ == '__main__':
    executeDemo()
