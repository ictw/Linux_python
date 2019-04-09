from selenium import webdriver

driver_path = r'/home/suofeiya/pycharm-2018.3.5/chromedriver'

# 用来修改一些Chrome的设置
options = webdriver.ChromeOptions()
options.add_argument("--proxy-server=http://115.218.208.198：9000")

# 将设置好的代理传入
driver = webdriver.Chrome(executable_path=driver_path, chrome_options=options)
driver.delete_all_cookies()
driver.get('http://httpbin.org/ip')


# 获取当前网站的Cookie信息
# for x in driver.get_cookies():
#     print(x)
#
# print('=' * 30)
# driver.delete_all_cookies()
# print(driver.get_cookie('BD_UPN'))
