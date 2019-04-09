import requests
from lxml import etree

header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36",
    "Referer": "https://movie.douban.com/"
}
url = 'https://movie.douban.com/cinema/nowplaying/linyi/'
response = requests.get(url, headers=header)
text = response.text

# print(response.text)    # 如果text出现乱码，要先使用content获取，然后使用decode来进行解码
# print(response.content) #直接从网络上抓取的数据，未经过解码。类型是byte类型

html = etree.HTML(text)
label_ul = html.xpath("//ul[@class='lists']")[0]
# print(etree.tostring(label_ul,encoding="UTF-8").decode("UTF-8"))
label_li = label_ul.xpath("./li")
movies = []
for li in label_li:
    title = li.xpath("@data-title")[0]
    score = li.xpath("@data-score")[0]
    region = li.xpath("@data-region")[0]
    director = li.xpath("@data-director")[0]
    actors = li.xpath("@data-actors")[0]
    image = li.xpath(".//img/@src")[0]
    movie = {
        "标题：": title,
        "评分：": score,
        "地区：": region,
        "导演：": director,
        "主演：": actors,
        "海报url：": image
    }
    movies.append(movie)
print(movies)
