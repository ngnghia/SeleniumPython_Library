from selenium import webdriver
import pytest
from Values.constant import *

class Driver:
    @pytest.fixture(autouse=True)
    def init_driver(self):
        # # get browser from config
        browser = CONFIG["Browser"][0]["name"]
        if browser == "chrome":
            self.driver = webdriver.Chrome()
        elif browser == "firefox":
            self.driver = webdriver.Firefox()
        elif browser == "edge":
            self.driver = webdriver.Edge()

        self.driver.get(CONFIG["URL"]["testing"])
        self.driver.maximize_window()
        yield self.driver
        if self.driver is not None:
            self.driver.close()

