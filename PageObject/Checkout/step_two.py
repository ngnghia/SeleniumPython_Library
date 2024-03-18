from selenium.webdriver.common.by import By
from Library.Commons import CommonMethods


class StepTwo(CommonMethods):
    def __init__(self, driver):
        self.driver = driver

    list_products = (By.XPATH, "*//div[@class='cart_item']")
    btn_fn        = (By.ID, "finish")
