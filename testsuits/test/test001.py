# 设置编码
# coding = utf-8

# 引入selenium 的webdriver包，导入webdriver包后才能使用webdriver API进行自动化脚本开发
from selenium import webdriver
# 导入时间模块time
import time

# 将控制的webdriver的Chrome（谷歌浏览器）赋值给browser，获得了浏览器对象,打开浏览器
browser = webdriver.Chrome(r'E:\Python\chromedriver_win32\chromedriver.exe')

# 获得浏览器对象后，通过get()方法，向浏览器发送网址，打开进入该网页
browser.get('https://www.taobao.com/')

browser.maximize_window()
browser.implicitly_wait(10)

# #J_Banner .banner-wrap a img
ele = browser.find_element_by_id('J_Banner')
print(ele)
