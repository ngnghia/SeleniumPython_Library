from selenium.webdriver.common.by import By
from Library.Commons import CommonMethods

class Login(CommonMethods):
    def __init__(self, driver):
        self.driver = driver

    txt_un = (By.ID, "user-name")
    txt_pw = (By.ID, "password")
    btn_login = (By.ID, "login-button")
