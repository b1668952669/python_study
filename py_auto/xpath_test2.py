from selenium import webdriver
import time

driver = webdriver.Chrome()
#访问QQ空间
driver.get('https://user.qzone.qq.com/3440210865')
time.sleep(10)

#点击课程目录   //*[@class="img_out_focus"]
#driver.find_element_by_xpath('//body//*[@class="face"]//*[@onerror="pt.qlogin.imgErr(this);"]').click()
#driver.find_element_by_xpath('id="switcher_plogin"').click()

#获取课程标题
titles = driver.find_elements_by_xpath('//*[@class="f-info qz_info_cut"]')
print(type(titles))

for title in titles:
    print(title.text)

#driver.quit()