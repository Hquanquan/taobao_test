import unittest
import time
from framework.browser import Browser
from pageobjects.taobaohomePage import TaobaoHomePage


class TaobaoHome(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """
        初始化操作
        打开浏览器
            1、实例化一个浏览器对象 browser
                1、先创建一个浏览器的类 Browser,已在frameword文件夹创建该类
                2、导入该类，使用from framework.browser import Browser导入，注意
                3、实例化对象 browser = Browser(cls)
            2、调用browser打开浏览器,并赋值给cls.driver使其成为该测试类的属性:
             cls.driver = browser.open_browser(cls)

        """
        cls.browser = Browser(cls)
        cls.driver = cls.browser.open_browser(cls)
        cls.taobaohomepage = TaobaoHomePage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        # cls.driver.quit()
        pass

    # 同步滑动滚动条至底部：模拟滑动
    @unittest.skip("暂不执行")
    def test6_execute_script(self):
        # 执行这段代码，会获取到当前窗口总高度
        js = "return action=document.body.scrollHeight"
        # 初始化现在滚动条所在高度为0
        height = 0
        # 当前窗口总高度
        new_height = self.driver.execute_script(js)
        while height < new_height:
            # 将滚动条调整至页面底部
            for i in range(height, new_height, 200):
                self.taobaohomepage.execute_script('window.scrollTo(0, {})'.format(i))
                time.sleep(0.5)
            height = new_height
            time.sleep(2)
            new_height = self.taobaohomepage.execute_script(js)

    # 滑动到有好货，随机点击有好货中的一项
    @unittest.skip('暂不执行')
    def test7_click_get_elements(self):
        el = self.driver.find_element_by_xpath('/html/body/div[5]/div/div[1]/div')
        time.sleep(2)
        self.taobaohomepage.slidingScrollbar(el)
        self.taobaohomepage.get_elements()

    #  验证是否为淘宝首页
    # @unittest.skip("暂不运行")
    def test1_getTaobaoHome_title(self):
        taobaotitle = self.taobaohomepage.get_url_title()
        self.assertEqual(taobaotitle, '淘宝网 - 淘！我喜欢')
        print(taobaotitle)

    # 鼠标悬停,点击连衣裙,打开新的页面，验证是不是连衣裙页面
    # @unittest.skip("暂不运行")
    def test2_moveOnElement(self):
        self.taobaohomepage.move_element()
        time.sleep(5)
        self.taobaohomepage.click_el()
        time.sleep(3)
        self.taobaohomepage.switch_to_window()

    # 搜索内衣
    @unittest.skip("暂不搜索")
    def test3_loginTaobaoPage(self):
        time.sleep(5)
        self.taobaohomepage.type_search('内衣')
        time.sleep(1)
        self.taobaohomepage.send_submit_btn()
        time.sleep(3)
        self.taobaohomepage.back_browser()

    # 点击banner
    @unittest.skip("暂不运行")
    def test4_clikc_banner(self):
        time.sleep(2)
        self.taobaohomepage.click_banner()
        self.taobaohomepage.switch_to_window()

    # 两种登录方式
    @unittest.skip("暂不运行")
    def test5_login1(self):
        self.taobaohomepage.login1()
        time.sleep(3)
        self.taobaohomepage.back_browser()
        time.sleep(2)
        self.taobaohomepage.login2()
        self.taobaohomepage.switch_to_window()


if __name__ == '__main__':
    unittest.main()
    unittest.main(verbosity=2)
