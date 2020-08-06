# -*- coding:utf-8 -*-
import os
import unittest
from selenium import webdriver

from framework.browser import Browser
from pageobjects.taobaoHomePage_top import TaoBaoHomePage_Top


class Demo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser(cls)
        cls.driver = cls.browser.open_browser(cls)
        cls.taobaohomepage = TaoBaoHomePage_Top(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        print("开始运行：")
        # driver = webdriver.Chrome(r'E:\Python\chromedriver_win32\chromedriver.exe')
        # driver.maximize_window()
        # driver.implicitly_wait(10)
        # driver.get("")

    def tearDown(self):
        print('结束运行')

    def test_001(self):
        self.taobaohomepage.isElementExist()


if __name__ == '__main__':
    unittest.main()
    unittest.main(verbosity=2)
