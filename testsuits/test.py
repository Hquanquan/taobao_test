# coding = utf-8
# import unittest
from selenium import webdriver
driver = webdriver.Chrome(r'E:\python\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://www.taobao.com/')

