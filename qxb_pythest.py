# coding=utf-8
import yaml
from appium import webdriver

from page.search_page import SearchPage


class TestDemo:
    scdata = yaml.safe_load(open("search_data.yaml","r"))
    print(scdata)
    def setup(self):
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
    # @pytest.mark.parametrize("keyword,jieguo",[("祖国",-1), ("中国",0 )])
    # def test_demo(self,keyword,jieguo):
    #     self.driver.find_element_by_id("com.intretech.readerx:id/tv_dialog_agreement_confirm").click()  # 点击“同意”按钮
    #     self.driver.find_element_by_id(
    #         "com.intretech.readerx:id/tv_welcome_look").click()  # 点击“我先看看”com.intretech.readerx:id/tv_welcome_look
    #     self.driver.find_element_by_xpath("//*[@text='搜索']").click()
    #     sousuo = self.driver.find_element_by_id("com.intretech.readerx:id/edit_search")
    #     sousuo.send_keys(keyword)
    #     self.driver.press_keycode(66)  # 回车键
    #     huiben = self.driver.find_elements_by_xpath("//*[@text='绘本']")
    #     assert len(huiben) > jieguo  #表示有搜到绘本，祖国只有歌曲，没有绘本


    def test_search_popage(self):
        search_page = SearchPage(self.driver)
        search_page.search("a")
        assert search_page.get_huiben() >= 0

class SearchPage(object):
    def __init__(self,driver):
        self.driver = driver
    def search(self,key):
        self.driver.find_element_by_id("com.intretech.readerx:id/tv_dialog_agreement_confirm").click()  # 点击“同意”按钮
        self.driver.find_element_by_id("com.intretech.readerx:id/tv_welcome_look").click()  # 点击“我先看看”com.intretech.readerx:id/tv_welcome_look
        self.driver.find_element_by_xpath("//*[@text='搜索']").click()
        self.driver.find_element_by_id("com.intretech.readerx:id/edit_search").send_keys(key)
        self.driver.press_keycode(66)
    def get_huiben(self):
        return len(self.driver.find_elements_by_xpath("//*[@text='绘本']"))


    # @pytest.mark.parametrize("keyword,jieguo", scdata)
    # def test_demo_from_yaml(self, keyword, jieguo):
    #     self.driver.find_element_by_id("com.intretech.readerx:id/tv_dialog_agreement_confirm").click()  # 点击“同意”按钮
    #     self.driver.find_element_by_id(
    #         "com.intretech.readerx:id/tv_welcome_look").click()  # 点击“我先看看”com.intretech.readerx:id/tv_welcome_look
    #     self.driver.find_element_by_xpath("//*[@text='搜索']").click()
    #     sousuo = self.driver.find_element_by_id("com.intretech.readerx:id/edit_search")
    #     sousuo.send_keys(keyword)
    #     self.driver.press_keycode(66)  # 回车键
    #     huiben = self.driver.find_elements_by_xpath("//*[@text='绘本']")
    #     assert len(huiben) > jieguo  # 表示有搜到绘本，祖国只有歌曲，没有绘本



#底下这部分yaml分离元素定位信息的，还没有搞明白，卡在用xpath定位不出元素来了
#     def test_demo_from_yaml(self):
#         TestCase("test_case.yaml").run(self.driver)
#
# class TestCase:
#     def __init__(self,path):
#         file = open(path,"r",encoding='utf-8')
#         self.steps = yaml.safe_load(file)
#
#     def run(self,driver:WebDriver):
#         for step in  self.steps:
#             element = None
#             if isinstance(step,dict):
#                 if "id" in step.keys():
#                     element = driver.find_element_by_id(step["id"])
#                 elif "xpath" in step.keys():
#                     element = driver.find_elements_by_id(step["xpath"])
#                 else:
#                     element.click()
#
#                 if "input" in step.keys():
#                     element.send_keys(step["input"])
#                     element.click()
#                     driver.press_keycode(66)  # 回车键
#                 else:
#                     element.click()







        # time.sleep(2)
        # sousuo.clear()
        # sousuo.send_keys("中国")
        # sousuo.click()
        # self.driver.press_keycode(66)  # 回车键
        # time.sleep(2)
        # assert "中国" in self.driver.find_element_by_xpath("//*[@text='中国美丽故事']").text
        # # assert len(self.driver.find_element_by_xpath("//*[countains(@text,'中国']")) >= 1     # 这样是错误的，为啥
        # print("搜索到的个数："+str(len(self.driver.find_elements_by_xpath("//*[@text='中国']"))) )
        # sousuo.clear()

        # sousuo.send_keys('hhhhh')
        # sousuo.click()
        # self.driver.press_keycode(66)  # 回车键
        # time.sleep(2)
        # sousuo.send_keys('中文清除')
        # sousuo.clear()
        # sousuo.send_keys('中文中国馆')
        # sousuo.click()
        # self.driver.press_keycode(66)  # 回车键
        # time.sleep(2)
        # search_cancel = self.driver.find_element_by_id("com.intretech.readerx:id/tv_search_cancel").click()  # 取消
        # self.driver.find_element_by_id("com.intretech.readerx:id/img_toolbar_main_avatar").click()  # 点击左上角头像返回登录页面
        # time.sleep(2)

    def teardown(self):
        self.driver.quit()



