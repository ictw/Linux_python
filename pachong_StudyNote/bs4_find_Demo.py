from bs4 import BeautifulSoup

html = """
<table class="tablelist" cellpadding="0" cellspacing="0">
		    	<tbody><tr class="h">
		    		<td class="l" width="374">职位名称</td>
		    		<td>职位类别</td>
		    		<td>人数</td>
		    		<td>地点</td>
		    		<td>发布时间</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47588&amp;keywords=&amp;tid=82&amp;lid=0">22989-运营产品中心高级产品经理</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47584&amp;keywords=&amp;tid=82&amp;lid=0">29912-数据产品经理</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47571&amp;keywords=&amp;tid=82&amp;lid=0">25929-沙盒游戏高级系统策划（深圳）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47573&amp;keywords=&amp;tid=82&amp;lid=0">23674-腾讯新闻客户端产品策划</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47566&amp;keywords=&amp;tid=82&amp;lid=0">30623-腾讯广告联盟广告品牌运营经理（北京）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>北京</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47544&amp;keywords=&amp;tid=82&amp;lid=0">CSIG02-腾讯云泛政府行业产品运营组组长（深圳）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47536&amp;keywords=&amp;tid=82&amp;lid=0">15575-《QQ三国》商业化活动运营（成都）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>成都</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47537&amp;keywords=&amp;tid=82&amp;lid=0">21309-企鹅辅导产品运营经理</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="even">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47538&amp;keywords=&amp;tid=82&amp;lid=0">22989-腾讯云高级项目经理（深圳）</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="odd">
		    		<td class="l square"><a target="_blank" href="position_detail.php?id=47534&amp;keywords=&amp;tid=82&amp;lid=0">18402-RPG手游市场运营</a></td>
					<td>产品/项目类</td>
					<td>1</td>
					<td>深圳</td>
					<td>2019-02-16</td>
		    	</tr>
		    			    	<tr class="f">
		    		<td colspan="5">
		    			<div class="left">共<span class="lightblue total">752</span>个职位</div>
		    			<div class="right"><div class="pagenav"><a href="javascript:;" class="noactive" id="prev">上一页</a><a class="active" href="javascript:;">1</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=10#a">2</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=20#a">3</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=30#a">4</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=40#a">5</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=50#a">6</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=60#a">7</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=70#a">...</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=750#a">76</a><a href="position.php?lid=&amp;tid=82&amp;keywords=请输入关键词&amp;start=10#a" id="next">下一页</a><div class="clr"></div></div></div>
		    			<div class="clr"></div>
		    		</td>
		    	</tr>
		    </tbody></table>

"""

bs = BeautifulSoup(html, 'lxml')

# 获取第二个tr标签
# trs = bs.find_all('tr',limit=2)[1]
# print(trs)

# 获取所有标签等于odd的ｔｒ标签,使用下划线与系统命名相同的区别开来,后面可以加多个判断条件
# trs = bs.find_all('tr', class_='odd')
# ａｔｔｒｉｂｕｔｅ属性
# trs = bs.find_all('tr', attrs={'class': 'odd'})
# for tr in trs:
#     print(tr)
#     print('=' * 30)

#
# a_List = bs.find_all('a')
# for href in a_List:
#     一：获取a标签下的所有href属性
#     print(href['href'])
# 　二：
# print(href.attrs['href'])
# print('=' * 30)

# 获取所有的职位信息
trs = bs.find_all('tr')[1:]
for tr in trs:
    tds = tr.find_all('td')
    # .string可以获取ｈｔｍｌ中的文本
    title = tds[0].string
    print(title)
    break

trs = bs.find_all('tr')[1:]
for tr in trs:
    # 　去除所有空白字符，输出生成器类型，可以将其转换为其他类型
    infos = list(tr.stripped_strings)
    # get_text输出文本形式
    print(infos)
