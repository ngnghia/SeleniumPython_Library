import sys, os, time
dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '/../../')
from PageObject.Checkout.step_one import StepOne
from PageObject.Checkout.step_two import StepTwo
from PageObject.Checkout.complete import Complete
from Driver.driver import Driver
from PageObject.Login.login import Login
from PageObject.HomePage.home import Home
from PageObject.Cart.cart import Cart
from Values.constant import *
import allure
class TestHome(Driver):

    @allure.story('HOME')
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.testcase(name="HO-02: Verify user can select any product then order and payment successfully", url='')
    def test_order_payment_successfully(self):
        '''
        Precondition: login system
        '''
        # new instance login class
        lg = Login(self.driver)
        # input valid username:
        lg.input_textbox(lg.txt_un, USERNAME)
        # input valid pw:
        lg.input_textbox(lg.txt_pw, PASSWORD)
        # click login
        lg.click_element(lg.btn_login)

        '''
          Select product by Name and click "Add to cart" button
         '''
        # init data
        product = {'Name': 'Sauce Labs Backpack', 'Price': '$29.99'}
        home = Home(self.driver)
        home.select_product_by_name(product['Name'])
        home.screenshot("select product")
        # Click Cart icon Take user to Cart page
        home.click_element(home.cart_link)
        home.screenshot("Cart list")

        '''
        On cart page, check product detail
        '''
        cart = Cart(self.driver)
        try:
            assert cart.check_product_detail(product) == True, "Product detail is not match"
        except Exception as e:
            print(e)

        #  Click check Out to jump to Check out Step one
        cart.click_element(cart.btn_checkout)

        '''
        On Step one page, input fields: First name, Last Name, Zip/Post Code
        '''
        step_1= StepOne(self.driver)
        step_1.input_textbox(step_1.txt_fn, "Michell")
        step_1.input_textbox(step_1.txt_ln, "Leon")
        step_1.input_textbox(step_1.txt_zc, "000111")
        step_1.screenshot("Checkout -Step one")
        # Click "Continue" Jump to Check out - Step Two page
        step_1.click_element(step_1.btn_continue)

        '''
        On Step Two page, observe the product list
        '''
        step_2 = StepTwo(self.driver)
        step_2.screenshot("Checkout -Step one")
        # Click "Finish" Jump to checkout Complete page
        step_2.click_element(step_2.btn_fn)

        '''
            Check Complete page
        '''
        complete = Complete(self.driver)
        step_2.screenshot("Complete")
        try:
            assert complete.verify_element_visible(complete.lbl_thank) == True, "Page is not displayed"
        except Exception as e:
            print(e)