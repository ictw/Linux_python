from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver_path = r'/home/suofeiya/pycharm-2018.3.5/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

inputTag = driver.find_element_by_id('kw')
inputTag.send_keys('hello,everyone, my name is suofeiya~')

# 隐式等待5s
# driver.implicitly_wait(5)

# 显式等待5s

WebDriverWait(driver, 5).until(
    # 只能传递一个参数，所以要使用元组的形式进行
    EC.presence_of_element_located((By.ID, 'sdau'))
)
