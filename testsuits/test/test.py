# -*- coding:utf-8 -*-
import os
import unittest
import sys


class Demo(unittest.TestCase):
    def setUp(self):
        print("开始运行：")

    def tearDown(self):
        print('结束运行')

    def test_0001_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0002_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0003_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0004_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0005_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0006_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_00070_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_00071_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0008_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0009_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0010_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0011_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0012_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0013_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0014_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0015_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)

    def test_0099_demo(self):
        print('当前函数的名称：%s ' % sys._getframe().f_code.co_name)
        print(os.getcwd())  # 获取当前工作目录路径
        print(os.path.abspath('.'))  # 获取当前工作目录路径
        # os.path.abspath('test.txt')  # 获取当前目录文件下的工作目录路径
        print(os.path.abspath('..'))  # 获取当前工作的父目录 ！注意是父目录路径
        print(os.path.abspath(os.curdir))  # 获取当前工作目录路径
        file = os.path.abspath('..') + '\\config\\config.ini'
        print(file)
        root_path = os.path.abspath(os.path.dirname(__file__)).split('taobao_test')[0] + 'taobao_test'
        print(root_path)

        # __file__获取执行文件相对路径，整行为取上一级的上一级目录
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(BASE_DIR)
#       新增一行,提交到本地仓库

if __name__ == '__main__':
    unittest.main()
    unittest.main(verbosity=2)
