import sys, os, time

dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '/../../')
from Driver.driver import Driver
from PageObject.Login.login import Login
from PageObject.HomePage.home import Home
from Values.constant import *
import allure

class TestLogin(Driver):

    @allure.story('LOGIN')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase(name="LG_01: login sucessful with valid credentals", url=CONFIG["URL"]['testing'])
    def test_login_successful(self):
        # new instance login class
        lg = Login(self.driver)
        # input valid username:
        lg.input_textbox(lg.txt_un, USERNAME)
        # input valid pw:
        lg.input_textbox(lg.txt_pw, PASSWORD)
        lg.screenshot('input credential')
        # click login
        lg.click_element(lg.btn_login)

        # check home page is displayed
        home = Home(self.driver)
        try:
            assert home.verify_element_visible(home.inventory) == True, "home page is not displayed"
        except Exception as e:
            print(e)
        lg.screenshot('Home page')

