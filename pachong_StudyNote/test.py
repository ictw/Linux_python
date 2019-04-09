# import base64
# import re
#
# s1 = base64.encodebytes(bytes('daimingyong244', 'utf-8'))
# # print(s1)
# s2 = base64.b64decode('ZGFpbWluZ3lvbmcyNDQ=\n')
# print(re.sub('\'|b','',str(s2)))


from selenium import webdriver

broswer = webdriver.PhantomJS

broswer.get(url='https://www.baidu.com')

print(broswer.current_url)