
# -*- coding:utf-8 -*-
# import unittest
from selenium import webdriver

driver = webdriver.Chrome(r'E:\python\chromedriver.exe')
# driver = webdriver.Chrome(chrome_options=chrome_options)

driver.implicitly_wait(10)

driver.maximize_window()

driver.get('https://www.taobao.com/')



# get_attribute('text')
# classname = driver.find_element_by_id('J_SiteNavSitemap').text
# print(classname)

# # //*[@id="J_SiteNavLogin"]/div[1]/div[2]
# user = driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[2]')
# login = driver.find_element_by_xpath('//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]')

# re = user.is_displayed()
# print(re)
# if not re:
#     print('该元素不可见')

# target = driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div')
# driver.execute_script("arguments[0].scrollIntoView();", target)



# driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/a[1]').text
# els = driver.find_elements_by_css_selector(".layer-inner .goods-inner ul a")

# els[0].click()

# for one in els:
#     one.click()


# import io  
# import sys 

# #改变标准输出的默认编码 
# #utf-8中文乱码
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030') 

