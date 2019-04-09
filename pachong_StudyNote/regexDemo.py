import re

# 正则表达式
text = 'hello everyone , my name is suofeiya.'
reg = re.match('hello', text)
# print(reg.group())

text = 'suofeiya'
reg = re.match('.', text)
# print(reg.group())

text = '3690'
reg = re.match('\d', text)
# print(reg.group())

text = ' '
# 匹配空白字符
reg = re.match('\s', text)
# print(reg.group())

text = 'abcABC123_'
reg = re.match('\w', text)
# print(reg.group())

text = 'hello-suofeiya'
reg = re.match('[\w\-]+', text)
# print(reg.group())


text = 'hello everyone,my name is suofeiya'
reg = re.match('[a-z]*', text)
# print(reg.group())


text = 'hello everyone,my name is suofeiya'
reg = re.match('[^a-z]+', text)
# print(reg.group())

text = 'hello everyone,my name is suofeiya'
reg = re.match('\w?', text)
# print(reg.group())

text = 'hello everyone,my name is suofeiya'
text = 'helloeveryone,mynameissuofeiya'
reg = re.match('\w(1)', text)
# print(reg.group())

# r代表raw，意思是原生
text = r'\n'
# print(text)
reg = re.match('', text)
# print(reg.group())
# 两层，第一层是正则表达式中的转义，第二层是python中的转义.
text = '\\n'
reg = re.match('\\\\n', text)
# print(text)

# group分组
text = 'hello everyone$123, my name is suofeiya$456.'
reg = re.search('.*(\d{3}).*(\d{3})', text)
# print(reg.group(0))
# print(reg.group(1, 2))
# groups除去第一个分组
# print(reg.groups())

text = 'hello everyone$1230,my name is suofeiya$4560.'
# reg=re.search()
reg = re.findall('\$\d+', text)
# sub替换
reg1 = re.sub('\$\d+', '000', text)
# print(reg, '\n', reg1)

# spilt函数用于提取,返回值为列表
text = 'hello everyone$,my name is suofeiya.'
reg = re.split(' |\$', text)
reg = re.split('[^\w]', text)
# print(reg)

# compile函数的使用
text = 'suofeiya\'s age is 21'
reg = re.compile('\d+')
re1 = re.search(reg, text)
# print(re1.group())

text = 'suofeiya has $2000.456'
# reg = re.compile('\$\d+\.\d+')
reg = re.compile(r"""
    \$ #匹配$符号
    \d+
    \.
    \d+
""", re.VERBOSE)
re1 = re.search(reg, text)
print(re1.group())
