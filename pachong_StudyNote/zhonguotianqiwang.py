import requests
from bs4 import BeautifulSoup
# from pyecharts.charts.bar import Bar
from pyecharts import Bar

ALL_DATA = []


def parse_page(url, index):
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
        'Referer': 'http://www.weather.com.cn/forecast/'
    }

    resp = requests.get(url, headers=headers)
    text = resp.content.decode('UTF-8')
    # 港澳台html不完整，需要容错性更高的html5lib来解析
    if index == 0:
        soup = BeautifulSoup(text, 'lxml')
    elif index == 1:
        soup = BeautifulSoup(text, 'html5lib')

    conMidtab = soup.find('div', class_='conMidtab')
    tables = conMidtab.find_all('table')
    for table in tables:
        trs = table.find_all('tr')[2:]
        for index, tr in enumerate(trs):
            tds = tr.find_all('td')
            if index == 0:
                city_name = list(tds[1].stripped_strings)[0]
            else:
                city_name = list(tds[0].stripped_strings)[0]
            min_temp = list(tds[-2].stripped_strings)[0]
            ALL_DATA.append({'城市': city_name, '最低温度': int(min_temp)})
            # print({'城市': city_name, '最低温低': min_temp})


def spider():
    areas = ['hb', 'db', 'hd', 'hz', 'hn', 'xb', 'xn']
    for area in areas:
        url = 'http://www.weather.com.cn/textFC/{}.shtml#'.format(area)
        parse_page(url=url, index=0)
        parse_page(url='http://www.weather.com.cn/textFC/gat.shtml#', index=1)

    # 根据最低气温进行排序
    # def sort_key(data):
    #     min_temp=data['最低温度']
    #     return min_temp
    ALL_DATA.sort(key=lambda data: data['最低温度'])
    data = ALL_DATA[0:10]
    # print(data)
    cities = list(map(lambda x: x['城市'], data))
    temps = list(map(lambda x: x['最低温度'], data))
    chart = Bar("中国天气最低气温榜")
    chart.add('', cities, temps)
    chart.render('中国天气最低气温榜.html')


# area = {
#     'hb': 1,
#     'db': 2,
#     'hd': 3,
#     'hz': 4,
#     'hn': 5,
#     'xb': 6,
#     'xn': 7,
#     'gat': 8
# }
# for key, value in area.items():
#     url = 'http://www.weather.com.cn/textFC/{}.shtml#'.format(key)
#     value += value
#     # parse_page(url,index=value)
#     print(value)


if __name__ == '__main__':
    try:
        spider()
    except Exception as e:
        print(e)
