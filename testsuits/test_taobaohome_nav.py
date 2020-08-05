# -*- coding:utf-8 -*-
import time
import unittest

# 为了导入自定义的包
# __file__获取执行文件相对路径，整行为取上一级的上一级目录
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.append(BASE_DIR)
from framework.browser import Browser
from pageobjects.taobaoHome_page import TaoBaoHomePage


class test_TaobaoHome_Page_nav(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.browser = Browser(cls)
        cls.driver = cls.browser.open_browser(cls)
        cls.taobaohomepage = TaoBaoHomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    # 判断是否是登录页面，然后返回上一页
    def isLoginPage(self):
        text = self.driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/a[1]').text
        self.assertEqual(text, "密码登录")
        # 验证通过，返回上一页
        self.taobaohomepage.back_browser()
        time.sleep(2)
        return True

    # @unittest.skip("暂不执行")
    def test000_move_to_nav_left_location(self):
        '''鼠标悬停中国大陆2秒,验证是否弹出列表'''
        self.taobaohomepage.move_to_nav_left_location()
        time.sleep(2)
        classname1 = self.driver.find_element_by_xpath('//*[@id="J_SiteNavBdL"]/li[1]').get_attribute("class")
        classname2 = "site-nav-menu site-nav-switch site-nav-multi-menu J_MultiMenu site-nav-menu-hover"
        self.assertEqual(classname1, classname2)

    # @unittest.skip("暂不执行")
    def test001_click_loginBtn1(self):
        """ 点击淘宝首页：亲，请登录，验证是否跳转到登录页 """
        self.taobaohomepage.click_nav__left_Login()
        self.isLoginPage()

    # @unittest.skip("暂不执行")
    def test002_click_nav_left_register(self):
        """ 点击免费注册，验证是否跳转到注册页面 """
        self.taobaohomepage.click_nav_left_register()
        time.sleep(2)
        title = self.taobaohomepage.get_url_title()
        self.assertEqual("账户注册 | 淘宝网", title)
        # 返回上一页
        self.taobaohomepage.back_browser()

    # @unittest.skip("暂不执行")
    def test003_click_nav_left_taobao(self):
        """ 点击手机逛淘宝，验证是否跳转到下载页面 """
        self.taobaohomepage.click_nav_left_taobao()
        time.sleep(2)
        title = self.taobaohomepage.get_url_title()
        self.assertEqual('PC下载页', title)
        # 返回上一页
        self.taobaohomepage.back_browser()

    # @unittest.skip("暂不执行")
    def test0040_move_nav_right_mytaobao(self):
        """  鼠标悬停在我的淘宝,验证是否弹出列表 """
        self.taobaohomepage.move_to_nav_right_mytaobao()
        time.sleep(2)

    # @unittest.skip("暂不执行")
    def test0041_click_nav_right_mytaobao(self):
        """  点击我的淘宝，验证是否跳转到登录页面 """
        self.taobaohomepage.click_nav_right_mytaobao()
        self.isLoginPage()

    # 
    # 未悬停前class=site-nav-menu site-nav-cart site-nav-menu-empty site-nav-multi-menu J_MultiMenu mini-cart menu
    # 悬停后class=site-nav-menu site-nav-cart site-nav-menu-empty site-nav-multi-menu J_MultiMenu mini-cart menu site-nav-menu-hover
    @unittest.skip("暂不执行")
    def test005_move_to_nav_right_cart(self):
        """ 鼠标悬停在购物车上，验证是否弹出相应的元素 """
        self.taobaohomepage.move_to_nav_right_cart()
        classname1 = self.driver.find_element_by_id("J_MiniCart").get_attribute("class")
        classname2 = 'site-nav-menu site-nav-cart site-nav-menu-empty site-nav-multi-menu J_MultiMenu mini-cart menu site-nav-menu-hover'
        self.assertEqual(classname1, classname2)
        time.sleep(2)

    # @unittest.skip("暂不执行")
    def test006_click_nav_right_cart(self):
        """ 点击购物车，验证是否跳转到登录页面 """
        self.taobaohomepage.click_nav_right_cart()
        self.isLoginPage()

    # @unittest.skip("暂不执行")
    def test0070_move_to_nav_right_J_SiteNavFavor(self):
        """  鼠标悬停收藏夹，验证是否弹出相应的元素 """
        self.taobaohomepage.move_to_nav_right_J_SiteNavFavor()
        classname1 = self.driver.find_element_by_id('J_SiteNavFavor').get_attribute('class')
        classname2 = 'site-nav-menu site-nav-favor site-nav-multi-menu J_MultiMenu site-nav-menu-hover'
        self.assertEqual(classname1, classname2)
        time.sleep(1)

    # @unittest.skip("暂不执行")
    def test0071_click_nav_right_J_SiteNavFavor(self):
        """ 点击收藏夹，验证是否跳转到登录页面 """
        self.taobaohomepage.click_nav_right_J_SiteNavFavor()
        self.isLoginPage()

    # @unittest.skip("暂不执行")
    def test008_click_nav_right_catalog(self):
        """ 点击商品分类，验证跳转到 淘宝首页行业市场 """
        self.taobaohomepage.click_nav_right_catalog()
        title = '淘宝首页行业市场'
        self.assertEqual(title, self.taobaohomepage.get_url_title())
        time.sleep(2)
        self.taobaohomepage.back_browser()

    # @unittest.skip("暂不执行") 
    def test0090_click_nav_right_J_SiteNavSeller(self):
        """ 点击牵牛卖家中心，验证是否跳转登录页面   """
        self.taobaohomepage.click_nav_right_J_SiteNavSeller()
        self.isLoginPage()

    # @unittest.skip("暂不执行")
    def test0091_move_to_nav_right_J_SiteNavSeller(self):
        """ 悬停牵牛卖家中心，验证弹出元素 """
        self.taobaohomepage.move_to_nav_right_J_SiteNavSeller()
        classname1 = self.driver.find_element_by_id('J_SiteNavSeller').get_attribute('class')
        classname2 = 'site-nav-menu site-nav-seller site-nav-multi-menu J_MultiMenu site-nav-menu-hover'
        self.assertEqual(classname1, classname2)
        time.sleep(1)

    # @unittest.skip("暂不执行")
    def test0092_click_el_J_SiteNavSeller(self):
        """ 随机点击牵牛卖家中心下面的元素 """
        self.taobaohomepage.click_el_J_SiteNavSeller()
        time.sleep(1)
        self.taobaohomepage.back_browser()

    # @unittest.skip("暂不执行")
    def test010_click_nav_right_J_SiteNavService(self):
        """ 点击联系客服，验证跳转 服务中心 """
        self.taobaohomepage.click_nav_right_J_SiteNavService()
        titel = '服务中心'
        self.assertEqual(titel, self.taobaohomepage.get_url_title())
        time.sleep(1)
        self.taobaohomepage.back_browser()

    # @unittest.skip("暂不执行")
    def test011_move_to_nav_right_J_SiteNavService(self):
        """ 悬停联系客服，验证弹出元素 """
        self.taobaohomepage.move_to_nav_right_J_SiteNavService()
        classname1 = self.driver.find_element_by_id('J_SiteNavService').get_attribute('class')
        classname2 = 'site-nav-menu site-nav-service site-nav-multi-menu J_MultiMenu site-nav-menu-hover'
        self.assertEqual(classname1, classname2)
        time.sleep(1)

    # @unittest.skip("暂不执行")
    def test012_click_el_nav_right_J_SiteNavService(self):
        """ 随机点击联系客服下的一个元素 """
        self.taobaohomepage.click_el_nav_right_J_SiteNavService()
        time.sleep(1)
        self.taobaohomepage.back_browser()

    # @unittest.skip("暂不执行")
    def test013_move_to_nav_right_J_SiteNavSitemap(self):
        """ 悬停网站导航,显示元素 """
        self.taobaohomepage.move_to_nav_right_J_SiteNavSitemap()
        classname1 = self.driver.find_element_by_id('J_SiteNavSitemap').get_attribute('class')
        classname2 = 'site-nav-menu site-nav-sitemap site-nav-multi-menu J_MultiMenu site-nav-menu-hover'
        self.assertEqual(classname1, classname2)
        time.sleep(1)

    # @unittest.skip("暂不执行")
    def test014_click_nav_right_J_SiteNavSitemap(self):
        """ 点击网站导航，验证跳转网址导航 """
        self.taobaohomepage.click_nav_right_J_SiteNavSitemap()
        title = '网址导航'
        self.assertEqual(title, self.taobaohomepage.get_url_title())
        time.sleep(1)
        self.taobaohomepage.back_browser()
        # 网址导航


if __name__ == '__main__':
    unittest.main()
    unittest.main(verbosity=2)
