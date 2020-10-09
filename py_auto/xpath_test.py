from selenium import webdriver

driver = webdriver.Chrome()
#访问腾讯课堂
driver.get('https://ke.qq.com/course/469093?tuin=b07f9b1d')

#点击课程目录
driver.find_element_by_xpath('//main//*[@ref="js_dir_tab"]').click()

#获取课程标题
titles = driver.find_elements_by_xpath('//*[@class="task-part-hd"]')
print(type(titles))

for title in titles:
    print(title.text)

driver.quit()