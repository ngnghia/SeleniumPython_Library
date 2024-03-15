import sys, os, time

from selenium.webdriver import Keys

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')
from Driver.driver import Driver
from PageObject.HomePage.home import Home
from Values.constant import *


class TestHomePage(Driver):

    '''
    '''
    def test_tabs(self):
        home = Home(self.driver)
        # new tab
        home.open_new_tab()
        home.switch_tab(1)
        self.driver.get("https://google.com")
        time.sleep(2)
        home.switch_tab(0)
        time.sleep(2)
        home.switch_tab(1)
        time.sleep(5)
