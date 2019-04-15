import requests
from lxml import etree
from fake_useragent import UserAgent

ua = UserAgent()

HEADER = {
    'User-Agent': ua.random
}
BASE_URL = 'https://www.80s.tw'


def get_detail_url(url):
    resp = requests.get(url, headers=HEADER)
    text = resp.text
    html = etree.HTML(text)
    detail_urls = html.xpath("//div[@id='body']//ul[@class='me1 clearfix']//h3//a/@href")
    detail_url = map(lambda url: BASE_URL + url, detail_urls)

    return detail_url


def get_detail_page(url):
    movies = {}
    resp = requests.get(url, headers=HEADER)
    text = resp.text
    html = etree.HTML(text)
    film_name = html.xpath("//div[@class='info']//h1[@class='font14w']/text()")[0]

    film_actor = html.xpath("//*[@id='minfo']/div[2]/span[3]/a/text()")
    download_url = html.xpath("//*[@id='myform']/ul/li[2]/span[2]/a/@href")

    movies['电影名：'] = film_name
    movies['主演：'] = film_actor
    movies['迅雷下载地址：'] = download_url

    return movies


def spider():
    base_url = 'https://www.80s.tw/movie/list/-----p/{}'
    for x in range(1, 6):
        print("========正在获取第" + str(x) + "页========")
        full_url = base_url.format(x)
        detail_urls = get_detail_url(full_url)
        for detail_url in detail_urls:
            movie = get_detail_page(detail_url)
            print(movie)

if __name__ == '__main__':
    try:
        spider()
    except Exception as e:
        print(e)
