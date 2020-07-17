from selenium.webdriver.remote.webdriver import WebDriver



#这个basepage页面的主要功能是封装其他页面都会用到的一些长用的方法，封装好给其他的调用，用继承的形式，class继承这个BasePage名字
class BasePage():

    #这个__init__是其页面也都会用到的，所以放在这里让其他页面调用
    def __init__(self,driver:WebDriver):
        self.driver = driver

    def find_element(self,locator):
        return self.driver.find_element(*(locator))
    # locator这个东西是用来放元素定位类型，和元素定位值的。前面加一个*号，意思是可以将它拆解，然后传给find_element使用。
    # 其他页面可以通过记成BasePage这个类，然后调用这个方法，但是前提是要先创建一个需要怎么定位的元素，元组内容包定位方式和定位内容，可参考其他页面
