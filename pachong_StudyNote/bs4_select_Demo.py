# ===========css选择器============
'''
1.根据标签查找，例如： p{
}
2.根据类名查找，例如： .line{
}
3.根据id名字查找，例如： #box{
}
4.查找子元素，例如： #box p{
}
5.查找直接子元素，例如： #box > p{
}
6.根据属性名查找，先写标签，中括号写属性值，例如： input[name='username']{
}
7.根据类名或者id号进行筛选，例如： div.line{}/div#line{}
'''

from bs4 import BeautifulSoup

tencent_html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
    <tbody>
    <tr class="h">
        <td class="l" width="374">职位名称</td>
        <td>职位类别</td>
        <td>人数</td>
        <td>地点</td>
        <td>发布时间</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47452&amp;keywords=&amp;tid=87&amp;lid=0">30359-视频业务运维工程师</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47448&amp;keywords=&amp;tid=87&amp;lid=0">TEG05-高级图像算法研究员（北京）</a>
        </td>
        <td>技术类</td>
        <td>2</td>
        <td>北京</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47450&amp;keywords=&amp;tid=87&amp;lid=0">15851-游戏测试工程师（深圳）</a>
        </td>
        <td>技术类</td>
        <td>3</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47451&amp;keywords=&amp;tid=87&amp;lid=0">15851-游戏专项测试开发工程师(深圳)</a>
        </td>
        <td>技术类</td>
        <td>3</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47443&amp;keywords=&amp;tid=87&amp;lid=0">28601-微信支付智能硬件专家</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47444&amp;keywords=&amp;tid=87&amp;lid=0">22989-腾讯云网络高级后台开发工程师（深圳）</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47434&amp;keywords=&amp;tid=87&amp;lid=0">23674-小程序web前端开发</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>北京</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47429&amp;keywords=&amp;tid=87&amp;lid=0">21527-腾讯音乐PHP应用开发工程师（深圳）</a>
        </td>
        <td>技术类</td>
        <td>2</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="even">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47423&amp;keywords=&amp;tid=87&amp;lid=0">TEG02-网络运维工程师</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="odd">
        <td class="l square"><a target="_blank" href="position_detail.php?id=47428&amp;keywords=&amp;tid=87&amp;lid=0">30628-腾讯广告算法高级工程师（研发中心-深圳）</a>
        </td>
        <td>技术类</td>
        <td>1</td>
        <td>深圳</td>
        <td>2019-02-13</td>
    </tr>
    <tr class="f">
        <td colspan="5">
            <div class="left">共<span class="lightblue total">1356</span>个职位</div>
            <div class="right">
                <div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active"
                                                                                                 href="javascript:;">1</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a">2</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=20#a">3</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=30#a">4</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=40#a">5</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=50#a">6</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=60#a">7</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=70#a">...</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=1350#a">136</a><a
                        href="position.php?lid=&amp;tid=87&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a>
                    <div class="clr"></div>
                </div>
            </div>
            <div class="clr"></div>
        </td>
    </tr>
    </tbody>
</table>
<p>
<!--hello，my name is suofeiya!!!-->
</p>

"""

bs = BeautifulSoup(tencent_html, 'lxml')
# 获取所有的tr标签
# trs = bs.select('tr')
# for tr in trs:
#     print(tr)
#     print('=' * 300)

# 获取第二个tr标签
# print(bs.select('tr')[1])

# trs = bs.select('.odd')
# trs=bs.select('tr[@class="even"]')
# for tr in trs:
#     print(trs)

# 获取所有a标签下的链接
# aList=bs.select('a')
# for a in aList:
#     href=a['href']
#     print(href)

# 获取所有文本信息
# trs = bs.select('tr')
# for tr in trs:
#     text = list(tr.stripped_strings)
#     print(text)
#     print('==' * 60)

# 获取注释
p = bs.find('p')
# contents返回的是list列表类型
print(p.contents[1])
