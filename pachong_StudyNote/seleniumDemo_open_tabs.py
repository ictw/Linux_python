from selenium import webdriver

driver_path = r'/home/suofeiya/pycharm-2018.3.5/chromedriver'
driver = webdriver.Chrome(executable_path=driver_path)
driver.get('https://www.baidu.com')

# 执行js，打开一个新的标签
driver.execute_script("window.open('https://douban.com')")

# 获取窗口句柄和driver的目标url
print('句柄' + str(driver.window_handles) + '\n' + driver.current_url)

# 标签之间的切换（Webdriver切换）
driver.switch_to.window(driver.window_handles[1])  # 后面的[x],x为索引

print(driver.current_url)
