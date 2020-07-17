# coding=utf-8
import yaml
from appium import webdriver

from page.app import App
from page.search_page import SearchPage


class TestDemo:
    def setup(self):
       self.search_page = App.start().to_search()

    def test_search_popage(self):
        self.search_page.search("a")
        assert self.search_page.get_huiben() >= 0

    def teardown(self):
        App.quit()



