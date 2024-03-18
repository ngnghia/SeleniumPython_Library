from selenium.webdriver.common.by import By
from Library.Commons import CommonMethods

class StepOne(CommonMethods):
    def __init__(self, driver):
        self.driver =driver

    txt_fn = (By.ID, "first-name")
    txt_ln = (By.ID, "last-name")
    txt_zc = (By.ID, 'postal-code')
    btn_continue = (By.ID, "continue")
