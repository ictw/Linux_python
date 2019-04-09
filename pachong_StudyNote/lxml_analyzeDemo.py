from lxml import etree


def parse_file():
    parser = etree.HTMLParser(encoding='UTF-8')
    htmlElement = etree.parse("./Other/lxml_Test.html", parser=parser)
    print(etree.tostring(htmlElement, encoding='UTF-8').decode('UTF-8'))
    with open('./Other/new.html', 'w') as file:
        file.write(etree.tostring(htmlElement, encoding='UTF-8').decode('UTF-8'))


def getLabel():
    parser = etree.HTMLParser(encoding='UTF-8')
    html = etree.parse("./Other/lxml_Test.html", parser=parser)
    # 获取所有标签,xpth返回的是列表
    """
    get_div = html.xpath("//span")
    for div in get_div:
        print(etree.tostring(div, encoding='UTF-8').decode('UTF-8'))
    """
    # 获取第二个标签
    """
    get_span = html.xpath("//span[2]")[0]
    # print(get_span)
    print(etree.tostring(get_span, encoding='UTF-8').decode('UTF-8'))
    
    """
    # 获取标签中的属性标签
    """
    get_class = html.xpath("//span[@class='oc']")
    for span in get_class:
        print(etree.tostring(span, encoding='UTF-8').decode('UTF-8'))
    """
    # 获取标签的特定属性的值
    """
    get_value=html.xpath("//div/@class")
    for value in get_value:
        print(value)
    """
    # 获取所有的职位信息——text
    tencent_html = etree.parse("./Other/tencent.html", parser=parser)
    get_trs = tencent_html.xpath("//tr[position()>1]")  # 排除第一个tr标签内容
    liebiao = []  # 定义一个列表将数据放入
    for trs in get_trs:
        href = trs.xpath(".//a/@href")[0]  # .代表当前标签下寻找，//则是在整个标签下寻找
        fullhref = 'https://hr.tencent.com' + href
        title = trs.xpath(".//a/text()")[0]  # 使用text()函数可以拿到文本
        # title=trs.xpath(".//td[1]//text()")   # 因为td标签不是文本内容的直接标，而属于a标签下的内容，所以不能直接获取，需要借助//来遍历td标签下的内容
        # print("职位： " + title)
        # print(etree.tostring(herf, encoding='UTF-8').decode('UTF-8'))
        work_type = trs.xpath(".//td/text()")[1]  # 放在里面td[x]也是可以的，但外面必须是[0]
        # print(work_type)

        dict = {
            '链接': fullhref,
            '职位：': title,
            '职位类型：': work_type
        }
        liebiao.append(dict)
    print(liebiao)


if __name__ == '__main__':
    getLabel()
