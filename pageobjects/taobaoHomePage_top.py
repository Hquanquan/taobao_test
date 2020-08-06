# -*- coding:utf-8 -*-
# 淘宝首页
import os
import sys

# __file__获取执行文件相对路径，整行为取上一级的上一级目录
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE_DIR)

import random
from units.base_page import BasePage


class TaoBaoHomePage_Top(BasePage):
    # 未登录时，亲，请登录 免费注册
    # 点击亲，请登录
    nav__left_Login = 'xpath=>//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[1]'

    def click_nav__left_Login(self):
        self.click(self.nav__left_Login)

    # 点击免费注册
    nav_left_register = 'xpath=>//*[@id="J_SiteNavLogin"]/div[1]/div[1]/a[2]'

    def click_nav_left_register(self):
        # 免费注册
        self.click(self.nav_left_register)

    # 已登录时，用户名称
    # 用户名称
    nav__left_user = 'xpath=>//*[@id="J_SiteNavLogin"]/div[1]/div[2]'

    # 鼠标悬停在用户名称上
    def move_to_nav__left_user(self):
        self.move_to_element(self.move_to_nav__left_user)

    # 点击用户名称
    def click_nav__left_user(self):
        self.click(self.nav__left_user)

    # ================
    # 中国大陆  一组元素
    nav_left_location = 'xpath=>//*[@id="J_SiteNavBdL"]/li[1]'

    # 鼠标悬停中国大陆
    def move_to_nav_left_location(self):
        self.move_to_element(self.nav_left_location)

    # 点击手机逛淘宝
    nav_left_taobao = 'id=>J_SiteNavMobile'

    def click_nav_left_taobao(self):
        # 手机逛淘宝
        self.click(self.nav_left_taobao)

    # 点击我的淘宝
    nav_right_mytaobao = 'id=>J_SiteNavMytaobao'

    def click_nav_right_mytaobao(self):
        # 我的淘宝
        self.click(self.nav_right_mytaobao)

    # 鼠标悬停在我的淘宝上
    def move_to_nav_right_mytaobao(self):
        self.move_to_element(self.nav_right_mytaobao)

    # 鼠标悬停在购物车上
    nav_right_cart = 'id=>J_MiniCart'

    def move_to_nav_right_cart(self):
        self.move_to_element(self.nav_right_cart)

    # 点击购物车
    def click_nav_right_cart(self):
        self.click(self.nav_right_cart)

    # 查看我的购物车
    nav_left_cart_tips = 's=>#J_MiniCart .site-nav-menu-bd .mini-cart-ft p a'

    # 收藏夹
    nav_right_J_SiteNavFavor = 'xpath=>//*[@id="J_SiteNavFavor"]'

    # 鼠标悬停在收藏夹
    def move_to_nav_right_J_SiteNavFavor(self):
        self.move_to_element(self.nav_right_J_SiteNavFavor)

    # 点击收藏夹
    def click_nav_right_J_SiteNavFavor(self):
        self.click(self.nav_right_J_SiteNavFavor)

    # 商品分类
    nav_right_catalog = 'xpath=>//*[@id="J_SiteNavCatalog"]/div/a/span'

    # 点击商品分类
    def click_nav_right_catalog(self):
        self.click(self.nav_right_catalog)

    # 牵牛卖家中心
    nav_right_J_SiteNavSeller = 'id=>J_SiteNavSeller'

    # 鼠标悬停，显示元素
    def move_to_nav_right_J_SiteNavSeller(self):
        self.move_to_element(self.nav_right_J_SiteNavSeller)

    # 点击牵牛卖家中心
    def click_nav_right_J_SiteNavSeller(self):
        self.click(self.nav_right_J_SiteNavSeller)

    # 牵牛卖家中心下的列表项 一组元素
    nav_right_J_SiteNavSeller_items = 's=>#J_SiteNavSeller .site-nav-menu-bd-panel a'

    # 随机点击一组数据中的一个数据
    def click_el_J_SiteNavSeller(self):
        els = self.find_elements(self.nav_right_J_SiteNavSeller_items)
        el = els[random.randint(1, len(els) - 1)]
        el.click()

    # 联系客服
    nav_right_J_SiteNavService = 'xpath=>//*[@id="J_SiteNavService"]/div[1]/a/span'
    # 联系客服下的列表项 一组元素
    nav_right_J_SiteNavService_items = 's=>#J_SiteNavService .site-nav-menu-bd-panel a'

    # 点击联系客服
    def click_nav_right_J_SiteNavService(self):
        self.click(self.nav_right_J_SiteNavService)

    # 悬停联系客服，显示元素
    def move_to_nav_right_J_SiteNavService(self):
        self.move_to_element(self.nav_right_J_SiteNavService)

    # 随机点击联系客服一组数据中的一个数据
    def click_el_nav_right_J_SiteNavService(self):
        els = self.find_elements(self.nav_right_J_SiteNavService_items)
        el = els[random.randint(1, len(els) - 1)]
        el.click()

    # 网站导航
    nav_right_J_SiteNavSitemap = 'xpath=>//*[@id="J_SiteNavSitemap"]/div[1]/a/span[2]'

    # 悬停网站导航
    def move_to_nav_right_J_SiteNavSitemap(self):
        self.move_to_element(self.nav_right_J_SiteNavSitemap)
    # 点击网站导航
    def click_nav_right_J_SiteNavSitemap(self):
        self.click(self.nav_right_J_SiteNavSitemap)

    # 顶部banner
    J_Banner = 's=>#J_Banner .banner-wrap a img'

    # 判断这个顶部banner元素是否存在页面中
    def isJ_BannerExist(self):
        flag = self.isElementExist(self.J_Banner)
        return flag


