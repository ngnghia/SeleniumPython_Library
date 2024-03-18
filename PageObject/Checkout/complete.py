from selenium.webdriver.common.by import By
from Library.Commons import CommonMethods


class Complete(CommonMethods):
    def __init__(self, driver):
        self.driver = driver
    lbl_thank = (By.CSS_SELECTOR, ".complete-header")
