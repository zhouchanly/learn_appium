from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page.base_page import BasePage


class SearchPage(BasePage):

    _input_locator = (By.ID,"com.intretech.readerx:id/edit_search") # 因为这个定位符会涉及到复用，直接放在某方法下，其他方法用不到，所以把它放到这个类下。通常会加一个下划线，表示私有变量，外面读取不到


    #这块内容放入BasePage页面，因为大家都有这块，然后class继承BasePage
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver
    def search(self,key):
        # self.driver.find_element_by_id("com.intretech.readerx:id/edit_search").send_keys(key)#这句话通过继承BasePage页面实现
        self.find_element(self._input_locator).send_keys(key)
        self.driver.press_keycode(66)
        return self
    def get_huiben(self):
        return len(self.driver.find_elements_by_xpath("//*[@text='绘本']"))

