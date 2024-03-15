from selenium import webdriver
import pytest
from Values.constant import *

class Driver:
    @pytest.fixture(autouse=True)
    def tc_setup(self):
        # # get browser from config
        # browser = CONFIG.get("Browser")[0].get("name")
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

