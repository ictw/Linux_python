import json
from multiprocessing import Queue
from handle_mongo import mongo_info
import requests

queue = Queue()


def handel_request(url, data):
    header = {
        'client': '4',
        'version': '6932.2',
        'device': '1801-A01',
        'sdk': '25,7.1.1',
        'imei': '866700031266685',
        'channel': '360box',
        # 'mac': '02:00:00:00:00:00',
        'resolution': '2160*1080',
        'dpi': '3.0',
        # 'android-id': '64cf6fa910cce7a1',
        # 'pseudo-id': '5355c2e6',
        'brand': '360',
        'scale': '3.0',
        'timezone': '28800',
        'language': 'en',
        'cns': '13',
        'carrier': 'China+Unicom',
        # 'imsi': '460014813320547',
        'user-agent': 'Mozilla/5.0(Linux;Android7.1.1;1801-A01Build/NMF26X;wv)AppleWebKit/537.36(KHTML,likeGecko)Version/4.0Chrome/59.0.3071.82MobileSafari/537.36',
        'reach': '1',
        'newbie': '1',
        # 'lon': '118.435386',
        # 'lat': '35.115056',
        # 'cid': '371300',
        'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
        'Accept-Encoding': 'gzip,deflate',
        'Connection': 'Keep-Alive',
        # 'Cookie': 'duid=58735735',
        'Host': 'api.douguo.net',
        # 'Content-Length': '65',
    }
    # 请求数据
    resp = requests.post(url=url, headers=header, data=data)
    # 创建一个队列
    return resp


def handle_index():
    url = 'http://api.douguo.net/recipe/flatcatalogs'
    data = {
        'client': '4',
        # '_session':'1549858873745866700031266685',
        'v': '1503650468',
        '_vs': '0',
    }
    response = handel_request(url=url, data=data)
    index_response_dict = json.loads(response.text)
    # 遍历json转换成的字典
    for index_item in index_response_dict['result']['cs']:
        for index_item_1 in index_item['cs']:
            for index_item_2 in index_item_1['cs']:
                data_2 = {
                    'client': '4',
                    # '_session':'1549858873745866700031266685',
                    'keyword': index_item_2['name'],
                    'order': '3',
                    '_vs': '400',
                }
                queue.put(data_2)


# 查看队列中一共有多少条数据
# print(queue.qsize())

def handle_caipu_list(data):
    print('当前处理的食材是: ', data['keyword'])
    caipu_list_url = 'http://api.douguo.net/recipe/v2/search/0/20'
    caipu_list_response = handel_request(url=caipu_list_url, data=data)
    caipu_list_response_dict = json.loads(caipu_list_response.text)
    for item in caipu_list_response_dict['result']['list']:
        caipu_info = {}
        caipu_info['食材:'] = data['keyword']
        if item['type'] == 13:
            caipu_info['作者:'] = item['r']['an']
            caipu_info['caipu_name']=item['r']['an']
            caipu_info['菜谱id:'] = item['r']['id']
            caipu_info['cookstory:'] = item['r']['cookstory'].replace('\n', '').replace(' ', '')
            caipu_info['所需材料:'] = item['r']['major']
            # print(caipu_info)
            detail_url = 'http://api.douguo.net/recipe/detail/' + str(caipu_info['菜谱id:'])
            detail_data = {
                'client': '4',
                # '_session': '1549870607619866700031266685',
                'author_id': '0',
                '_vs': '2803',
                '_ext': '{"query":{"kw":' + data['keyword'] + ',"src":"2803","idx":"1","type":"13","id":' + str(
                    caipu_info['菜谱id:']) + '}}',
            }
            detail_response = handel_request(url=detail_url, data=detail_data)
            detail_dict = json.loads(detail_response.text)
            caipu_info['tips:'] = detail_dict['result']['recipe']['tips']
            caipu_info['制作步骤: '] = detail_dict['result']['recipe']['cookstep']
            print(json.dumps(caipu_info))
            # 入库m
            print('当前入库的菜谱是:', caipu_info['caipu_name'])
            mongo_info.insert_item(caipu_info)
            # print(detail_url)
        else:
            continue


handle_index()
handle_caipu_list(queue.get())
