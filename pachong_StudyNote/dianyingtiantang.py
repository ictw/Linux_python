from lxml import etree
import requests
# 使用UserAgent库来随机
from fake_useragent import UserAgent
import queue

ua = UserAgent()
BASE_URL = "https://www.dytt8.net"
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
    'Referer': 'https://www.dytt8.net/html/gndy/dyzz/index.html'
}


def get_detail_url(url):
    response = requests.get(url=url, headers=HEADERS)
    # 可以在开发者工具中使用document.charset来查看网页编码格式
    # 第一页中含有特殊字符，无法使用gbk解码，所以使用系统默认
    # text = response.content.decode("GBK")
    text = response.text
    html = etree.HTML(text)
    last_url = html.xpath("//table[@class='tbspan']//a/@href")
    # print(BASE_URL + str(last_url))
    # for url in movie_url:
    detail_url = map(lambda url: BASE_URL + url, last_url)
    return detail_url


def parse_detail_page(url):
    try:
        movies = {}
        response = requests.get(url, headers=HEADERS)
        text = response.content.decode("gbk")
        html = etree.HTML(text)
        title = html.xpath("//div[@class='title_all']//font[@color='#07519a']/text()")[0]
        # test_title
        # print(title)
        div_Zoom = html.xpath("//div[@id='Zoom']")[0]
        picture = div_Zoom.xpath(".//img/@src")
        movie_detail = div_Zoom.xpath(".//text()")

        for index, info in enumerate(movie_detail):

            # 提取以特定字符串开头的数据
            if info.startswith("◎年　　代"):
                # 将不必要的数据删除，并去除前后空格
                year = info.replace("◎年　　代", "").strip()
                movies['上映时间：'] = year

            elif info.startswith("◎产　　地"):
                shangyingdiqu = info.replace("◎产　　地", "").strip()
                movies['上映地区：'] = shangyingdiqu

            elif info.startswith("◎主　　演"):
                actors = info.replace("◎主　　演", "").strip()
                actors_list = [actors]
                for i in range(index + 1, len(movie_detail)):
                    actor = movie_detail[i].strip()
                    if actor.startswith("◎"):
                        break
                    actors_list.append(actor)
                movies['主演：'] = actors_list

            elif info.startswith("◎简　　介"):
                jianjie = info.replace("◎简　　介", "").strip()
                for jj in range(index + 1, len(movie_detail)):
                    profile = movie_detail[jj].strip()
                    if profile.startswith("【下载地址】"):
                        break
                    movies['简介：'] = profile
                # print(movies['简介：'])

        download_url = div_Zoom.xpath(".//a/@href")

        movies['电影名：'] = title
        movies['海报：'] = picture[0]
        movies['电影截图：'] = picture[1]
        movies['磁力链接：'] = download_url[0]
        movies['ftp链接：'] = download_url[1]

        print(movies)
    except Exception as e:
        print(e)

    # return movies
    # print(movie_detail
    # )

    # for i in title:
    #     print(etree.tostring(i,encoding="UTF-8").decode("UTF-8"))


def spider():
    base_url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
    movies = []
    for x in range(1, 8):
        url = base_url.format(x)
        # movies = parse_detail_page(url)
        print("=====当前是第" + str(x) + "页======")
        detail_urls = get_detail_url(url)
        # 遍历详情url
        try:
            for detail_url in detail_urls:
                # print(detail_url)
                # movie = parse_detail_page(detail_url)
                parse_detail_page(detail_url)
            # movies.append(movie)
            # print(movie)
            # with open('./Other/dianyingtiantang.txt', 'a+') as file:
            #     file.write(str(movie))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    try:
        spider()
    except Exception as e:
        print(e)
