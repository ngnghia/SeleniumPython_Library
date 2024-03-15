import sys, os, time

dir = os.path.dirname(__file__)
sys.path.insert(0, dir + '/../')
from Driver.driver import Driver
from PageObject.HomePage.blog import Blog
from Values.constant import *
from Library.FileHelper import FileHelp
import allure

class Test_Blog(Driver):

    @allure.story('Chức năng đăng nhập')
    @allure.testcase(name="TC: Login", url="")
    def test_input_login(self):        # new instance for Blog class
        vblog = Blog(self.driver)
        '''=========================================
        TEST for  "Simple Login Page" sesson
        ========================================='''
        #  1. Scroll to section "Simple Login Page"
        #  - type username & password
        vblog.input_textbox(vblog.txt_username, USERNAME)
        vblog.move_to_element(vblog.form_login)
        vblog.input_textbox(vblog.txt_password, PASSWORD)
        vblog.screenshot("login section")
        #  - login + close alert
        vblog.click_element(vblog.btn_login)
        time.sleep(5)
        vblog.screenshot("open alert")
        vblog.close_alert(True)
        #  - cancel + check textbox is empty
        vblog.click_element(vblog.btn_cancel)
        vblog.screenshot("cancel to clear textbox")
        try:
            # check textbox empty after clear
            assert vblog.get_value_textbox(vblog.txt_username) == "", "username is not empty"
            assert vblog.get_value_textbox(vblog.txt_password) == "", "password is not empty"
        except Exception as e:
            print(e)


    @allure.story('Home Pages')
    @allure.testcase(name="Loop and print table values", url="")
    def test_print_table_values(self):
        # new instance for Blog class
        vblog = Blog(self.driver)

        # 2. Move to Table and print all text of rows
        vblog.move_to_element(vblog.table)
        vblog.read_table_data()
        vblog.screenshot("data table")

    @allure.story('Home Pages')
    @allure.testcase(name="switch iframes",url="")
    def test_iframe(self):
        # new instance for Blog class
        vblog = Blog(self.driver)

        # 4. Move to frame 1 & frame 2 check they are visible
        vblog.switch_to_frame(vblog.frame1)
        vblog.switch_to_default()
        vblog.switch_to_frame(vblog.frame2)
        vblog.switch_to_default()
        vblog.screenshot("iframe")

    @allure.story('Home Pages')
    @allure.testcase(name="test checkbox & radio is selected" , url="")
    def test_radio_checkbox(self):
        # new instance for Blog class
        vblog = Blog(self.driver)
        '''
        ======== at the right panel ==========
        ====== ====== ====== ====== ====== ======
        5. section of checkbox: click 1 checkbox Orange + verify is selected
        6.click 1 radio Male + verify is selected
        '''
        vblog.click_element(vblog.radio1)
        vblog.click_element(vblog.chbox2)
        vblog.screenshot("radio & check box")
        try:
            assert vblog.verify_element_selected(vblog.radio1) == True, "not yet selected"
            assert vblog.verify_element_selected(vblog.chbox2) == True, "not yet selected"
        except Exception as e:
            print(e)

        '''
        7. move to double click + verify list presence
        '''

    @allure.story('Home Pages')
    @allure.testcase(name="double click", url="")
    def test_double_click(self):
            # new instance for Blog class
        vblog = Blog(self.driver)

        vblog.move_to_element(vblog.link_dup_click)
        vblog.double_click_element(vblog.link_dup_click)
        try:
            assert vblog.verify_element_visible(vblog.droplist_delay) == True, "element is not displayed"
        except Exception as e:
            print(e)

        '''
        ================= at the lelf panel  ======================
        ================= at the lelf panel  ======================
         1. Move to Multi option,  select 1 or n item
        '''

    @allure.story('Home Pages')
    @allure.testcase(name="Multi select", url="")
    def test_multi_select(self):
        # new instance for Blog class
        vblog = Blog(self.driver)

        vblog.move_to_element(vblog.select)
        vblog.select_droplist_by_value(vblog.select, "volvox")

        '''
        2. droplist "Older Newsletters":
         select any item and check selected item
        '''

    @allure.story('Home Pages')
    @allure.testcase(name="droplist: select one item and selected text", url="")
    def test_select_droplist(self):
        # new instance for Blog class
        vblog = Blog(self.driver)
        vblog.select_droplist_by_text(vblog.droplist, "doc 2")
        try:
            assert vblog.get_text_selected_item_drl(vblog.droplist).strip().lower() == "doc 2", "checking item not match"
        except Exception as e:
            print(e)

        '''
        4. Open new  window.
          - click link
          - switch to new tab
          - switch back old tab
        '''

    @allure.story('Home Page')
    @allure.testcase(name="open new tab", url="")
    def test_open_newtab(self):
        # new instance for Blog class
        vblog = Blog(self.driver)
        vblog.move_to_element(vblog.link_SeleniumTutorial)
        vblog.click_element(vblog.link_SeleniumTutorial)
        self.driver.back()

    @allure.story('Home Page')
    @allure.testcase(name="check button is disable/ enable", url="")
    def test_element_disable_enable(self):
        # new instance for Blog class
        vblog = Blog(self.driver)
        try:
            assert vblog.verify_element_enable(vblog.btn1_button) == False, "button is not disabled"
            assert vblog.verify_element_enable(vblog.btn2_button) == True, "button is not enabled"
            # check text box disabled
            assert vblog.verify_element_enable(vblog.txt_tb2) == False, "textbox is not enabled"
        except Exception as e:
            print(e)
        '''
        read data from order list
        '''
    @allure.story('Home Page')
    @allure.testcase(name="get items of order list", url="")
    def test_read_data_orderlist(self):
        # new instance for Blog class
        vblog = Blog(self.driver)
        vblog.read_data_droplist()

        '''
        8. Popup window.
        '''
    @allure.story('Home Page')
    @allure.testcase(name="switch new window", url="")
    def test_switch_window(self):
        # new instance for Blog class
        vblog = Blog(self.driver)
        vblog.click_element(vblog.link_popup)
        vblog.switch_to_window()
        vblog.switch_to_window(False)

        '''
         9. Upload file
        '''
    @allure.story('Home Page')
    @allure.testcase(name="upload file", url="")
    def test_upload_file(self):
        # new instance for Blog class
        vblog = Blog(self.driver)
        vblog.move_to_element(vblog.btn_upload_file)
        vblog.click_element_Actions(vblog.btn_upload_file)
        help = FileHelp()
        help.upload_file(FILE1)