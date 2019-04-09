import time
from selenium import webdriver
from selenium.webdriver.common.by import By
# 操作下拉菜单的表单元素所需要的包
from selenium.webdriver.common.keys import Keys

driver_path = r'/home/suofeiya/pycharm-2018.3.5/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

# 获取网站的源代码
print(driver.page_source)

# 按照条件查找元素
# inputTag = driver.find_element_by_id('kw')
inputTag_1 = driver.find_element(By.NAME, 'wd')

inputTag_1.send_keys('hello,everyone my name is suofeiya~')

time.sleep(1)
# 第一种方式进行检索
inputTag_1.send_keys(Keys.ENTER)
# 第二种方式进行检索
# enterTag = driver.find_element_by_id("su").click()

time.sleep(1)

driver.quit()
