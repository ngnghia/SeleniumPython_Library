from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Library.Commons import CommonMethods

class Login(CommonMethods):
    def __init__(self, driver):
        self.driver = driver

    txt_un = (By.ID, "user-name")
    txt_pw = (By.ID, "password")
    btn_login = (By.ID, "login-button")
