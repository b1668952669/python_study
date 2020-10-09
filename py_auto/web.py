from selenium import webdriver


driver = webdriver.Chrome()

#访问百度首页
driver.get("https://www.baidu.com/")

#知道到百度首页的输入框
ele = driver.find_element_by_id("kw")


#输入内容chromedriver
ele.send_keys("chromedriver")

#点击搜索
driver.find_element_by_id("su").click()