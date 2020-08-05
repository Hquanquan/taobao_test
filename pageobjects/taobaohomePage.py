# 淘宝首页
import os
import sys

# __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import random
from units.base_page import BasePage

"""
 页面类，主要存放页面的元素定位和简单的操作函数.
 页面类主要是元素定位和页面操作写成函数，以供测试类使用
 集成 BasePage 二次封装通用类
 通常 1个页面为一个类
"""


# 淘宝首页类
class TaobaoHomePage(BasePage):
    # ================

    # 随机选择有好货这一组元素中的一个，点击
    els2 = "s=>.layer-inner .goods-inner ul a"

    def get_elements(self):
        els = self.find_elements(self.els2)
        # 随机选择这一组元素中的一个[random.randint(1, len(els) - 1)]
        el = els[random.randint(1, len(els) - 1)]
        el.click()

    # =============================

    banner1 = 'xpath=>//*[@id="tanxssp-outer-conmm_12852562_1778064_13670999"]/a/img'

    def click_banner(self):
        self.click(self.banner1)

    # ===============
    # 亲，请登录按钮
    loginBtn1 = 'xpath=>//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]'
    # 右侧登录按钮
    loginBtn2 = 'xpath=>/html/body/div[4]/div[2]/div[1]/div/div[2]/div[1]/a[1]'

    def login1(self):
        self.click(self.loginBtn1)

    def login2(self):
        self.click(self.loginBtn2)

    # ===========================================
    els = 'xpath=>/html/body/div[4]/div[1]/div/div[1]/div/ul/li[1]'
    el = 'xpath=>/html/body/div[4]/div[1]/div/div[1]/div/div/div[1]/div[1]/div[1]/p/a[1]'

    # 鼠标悬停
    def move_element(self):
        self.move_to_element(self.els)

    def click_el(self):
        self.click(self.el)

    # ==================================================
    # 输入框
    inputbox = 'xpath=>//*[@id="q"]'
    # 搜索按钮
    btn = 'xpath=>//*[@id="J_TSearchForm"]/div[1]/button'

    # 输入框输入搜索内容
    def type_search(self, text):
        self.send_keys(self.inputbox, text)  # 传递文本框 id 和 内容

    # 点击搜索按钮
    def send_submit_btn(self):
        self.click(self.btn)

# =========================================
