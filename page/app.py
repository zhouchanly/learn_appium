from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from page.main_page import MainPage


class App:
    driver:WebDriver = None
    @classmethod
    def start(cls):
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

        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(10)

        cls.driver.find_element_by_id("com.intretech.readerx:id/tv_dialog_agreement_confirm").click()  # 点击“同意”按钮
        cls.driver.find_element_by_id("com.intretech.readerx:id/tv_welcome_look").click()  # 点击“我先看看”com.intretech.readerx:id/tv_welcome_look

        return MainPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()

