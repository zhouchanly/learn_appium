from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page.base_page import BasePage
from page.search_page import SearchPage


class MainPage(BasePage):
    _search_locator = (By.XPATH, "//*[@text='搜索']")  # 因为这个定位符会涉及到复用，直接放在某方法下，其他方法用不到，所以把它放到这个类下。通常会加一个下划线，表示私有变量，外面读取不到
    _search_icon_locator = (By.ID,"com.intretech.readerx:id/img_main_search_icon")
    # 这块内容放入BasePage页面，因为大家都有这块，然后class继承BasePage
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver
    def to_search(self):
        self.driver.find_element_by_xpath("//*[@text='搜索']").click()  #这句话通过继承BasePage页面实现为以下方式

        #self.driver.find_element(self._search_icon_locator).click()    #这句话一直运行不了，提示“selenium.common.exceptions.InvalidSelectorException: Message: Locator Strategy 'id,com.intretech.readerx:id/img_main_search_icon' is not supported for this session”
        return SearchPage(self.driver)