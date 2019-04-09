# selenium行为链
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver_path = r'/home/suofeiya/pycharm-2018.3.5/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

inputTag = driver.find_element_by_id('kw')
submitBtn = driver.find_element_by_id('su')

actions = ActionChains(driver)
actions.move_to_element(inputTag)
actions.send_keys_to_element(inputTag, 'hello,everyone, my name is suofeiya~')
actions.move_to_element(submitBtn).click()

"""
更多用法：
https://seleniumhq.github.io/selenium/docs/api/py/api.html
"""
# 执行行为链
actions.perform()
