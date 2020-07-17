# coding=utf-8
from appium import webdriver
import time
from unittest import TestCase

class TestDemo(TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = '127.0.0.1:62001'
        desired_caps['appPackage'] = 'com.intretech.readerx'
        desired_caps['appActivity'] = 'com.intretech.readerx.ui.WelcomeActivity'
        desired_caps['automationName'] = 'uiautomator2'
        desired_caps['newCommandTimeout'] = "2000"
        desired_caps["unicodeKeyboard"] = True  # 使用unicode编码方式发送字符串
        desired_caps["resetKeyboard"] = True  # 隐藏键盘

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(10)

    def test_demo(self):
        self.driver.find_element_by_id("com.intretech.readerx:id/tv_dialog_agreement_confirm").click()  # 点击“同意”按钮
        self.driver.find_element_by_id(
            "com.intretech.readerx:id/tv_welcome_look").click()  # 点击“我先看看”com.intretech.readerx:id/tv_welcome_look
        self.driver.find_element_by_xpath("//*[@text='搜索']").click()
        sousuo = self.driver.find_element_by_id("com.intretech.readerx:id/edit_search")
        sousuo.send_keys('hh')
        self.driver.press_keycode(66)  # 回车键
        time.sleep(2)
        sousuo.send_keys('中文清除')
        sousuo.clear()
        sousuo.send_keys('中文')
        self.driver.press_keycode(66)  # 回车键
        time.sleep(2)
        search_cancel = self.driver.find_element_by_id("com.intretech.readerx:id/tv_search_cancel").click()  # 取消
        self.driver.find_element_by_id("com.intretech.readerx:id/img_toolbar_main_avatar").click()  # 点击左上角头像返回登录页面
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()





