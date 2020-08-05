# 1、导入相关的模块
import unittest
import HTMLTestRunner
import os
from datetime import date
# from test_taobaoHome import TaobaoHome
from test_taobaohome_nav import test_TaobaoHome_Page_nav

# 保存文件的设置
# 获取当天日期
now = date.today()
# 格式化日期
dateStr = now.strftime('%Y-%m-%d')
# 获取当前运行文件的上一级目录
dir = os.path.abspath('..')

# 2、加载被测模块里的测试类
search_test = unittest.TestLoader().loadTestsFromTestCase(test_TaobaoHome_Page_nav)

# 3、添加被测模块到unittest.TestSuite([a,b]),以数组的形式传参
smoke_tests = unittest.TestSuite(search_test)
#  4、TestRunner运行测试
# unittest.TextTestRunner(verbosity=2).run(smoke_tests)
# 使用HTMLTestRunner代替默认的unittest.TextTestRunner()执行测试用例即可
#  5、写入测试结果
# 创建保存文件的路径
filepath = dir + "\\test_reports\\SmokeTestReport{}.html".format(dateStr)
print(filepath)
with open(filepath, 'wb') as outfile:
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile, title='标题：淘宝首页导航栏-冒烟测试',
                                           description='描述：未登录情况下，淘宝首页导航栏的各项功能')
    runner.run(smoke_tests)
