import time

import requests
from selenium.common import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
import pyautogui
import allure
from Values.constant import CONFIG

class CommonMethods:

    def __init__(self, driver):
        self.driver = driver
    '''
      Common methods to interact with web element
    '''
    # input textbox, need to pass locator and value
    def input_textbox(self, locator, value):
        try:
            self.wait_for_element_visible(locator)
            e = self.driver.find_element(*locator)
            e.clear()
            e.send_keys(value)
        except Exception as e:
            print(e)

    # get value from textbox, need to pass locator and value
    def get_value_textbox(self, locator):
        try:
            self.wait_for_element_visible(locator)
            e = self.driver.find_element(*locator)
            return e.get_attribute("value").strip()
        except Exception as e:
            return ''

    # get test from label, link ...
    def get_text_element(self, locator):
        try:
            self.wait_for_element_visible(locator)
            e = self.driver.find_element(*locator)
            return e.text.strip()
        except Exception as e:
            return ''

    def click_element(self, locator):
        try:
            self.wait_for_element_visible(locator)
            self.driver.find_element(*locator).click()
        except Exception as e:
            print(e)

    def click_element_Actions(self, locator):
        try:
            self.wait_for_element_visible(locator)
            ActionChains(self.driver).move_to_element(self.driver.find_element(*locator)).click().perform()
        except Exception as e:
            print(e)

    def double_click_element(self, locator):
        try:
            self.wait_for_element_visible(locator)
            ActionChains(self.driver).double_click(self.driver.find_element(*locator)).perform()
        except Exception as e:
            print(e)

    # verify checkbox or element is selected?
    def verify_element_selected(self, locator):
        try:
            self.wait_for_element_visible(locator)
            if self.driver.find_element(*locator).is_selected():
                return True
            else:
                return False
        except Exception as e:
            print(e)

    def verify_element_presence(self, locator):
        try:
            self.wait_for_element_precense(locator)
            return self.driver.find_element(*locator).is_presence()
        except Exception as e:
            return False

    def verify_element_visible(self, locator):
        try:
            self.wait_for_element_visible(locator)
            return self.driver.find_element(*locator).is_displayed()
        except Exception as e:
            return False

    '''
        check element is enable 
    '''
    def verify_element_enable(self, locator):
        try:
            self.wait_for_element_precense(locator)
            return self.driver.find_element(*locator).is_enabled()
        except Exception as e:
            print(e)

    '''
        # select value from droplist
        used for simply droplist has id.
        get url for test this method https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407
    '''
    def select_droplist_by_value(self, locator, value):
        try:
            self.wait_for_element_visible(locator)
            Select(self.driver.find_element(*locator)).select_by_value(value)
        except Exception as e:
            print(e)

    def select_droplist_by_index(self, locator, value):
        try:
            self.wait_for_element_visible(locator)
            Select(self.driver.find_element(*locator)).select_by_index(value)
        except Exception as e:
            print(e)

    def select_droplist_by_text(self, locator, value):
        try:
            self.wait_for_element_visible(locator)
            Select(self.driver.find_element(*locator)).select_by_visible_text(value)
        except Exception as e:
            print(e)

    # get text of selected item in droplist
    def get_text_selected_item_drl(self, locator):
        try:
            self.wait_for_element_visible(locator)
            return Select(self.driver.find_element(*locator)).first_selected_option.text
        except Exception as e:
            print(e)

    # return list of element has the same locator exam: "*//ul/li[@class='_3D0G9a']")
    def get_element_list(self, locator):
        try:
            self.wait_for_element_visible(locator)
            return self.driver.find_elements(*locator)
        except Exception as e:
            print(e)

    # upload file button and window,
    def upload_file_button(self, locator, pathfile):
        try:
            self.wait_for_element_visible(locator)
            self.driver.find_element(*locator).click()
            pyautogui.write(pathfile)
            pyautogui.press('enter')
        except Exception as e:
            print(e)

    # select alert, if True = accept, False = dismiss
    '''
        this method apply for simple alert has id/ name. use url for test https://omayo.blogspot.com/
        ----------
        If other system implements complex alert() will need find locator of cancel/ ok options for selecting. 
        So accept()/dismiss() unable apply in this case.
    '''
    def close_alert(self, accept=True):
        try:
            time.sleep(2)
            if accept:
                self.driver.switch_to.alert.accept()
            else:
                self.driver.switch_to.alert.dismiss()
        except Exception as e:
             print(e)

    '''
        this method apply for alert with textbox()
    '''
    def click_prompt_textbox(self, locator, value =""):
        try:
            self.wait_for_element_visible(locator)
            self.driver.find_element(*locator).click()
            time.sleep(2)
            obj = self.driver.switch_to.alert
            obj.send_keys(value)
            obj.accept()
        except Exception as e:
            print(e)
    '''
    apply for frame has id/ name have a look https://the-internet.herokuapp.com/nested_frames
    '''
    def switch_to_frame(self, locator):
        try:
            WebDriverWait(self.driver, CONFIG.get("TimeOut").get("explicit")).until((EC.frame_to_be_available_and_switch_to_it(locator)))
        except Exception as e:
            print(e)

    '''
     once completed testing activities in frame, use this method to comback current page
    '''
    def switch_to_default(self):
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(e)

    '''
        switch to between windows. default True switch to new window, else back parent  
    '''
    def switch_to_window(self, new_window=True):
        if new_window:
            self.driver.switch_to.window(self.driver.window_handles[1])
        else:
            self.driver.switch_to.window(self.driver.window_handles[0])


    # WAIT ELEMENT visible BEFORE do test
    def wait_for_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 30).until((EC.visibility_of_all_elements_located(locator)))
        except TimeoutException:
            print("it took so long to load")

    # WAIT ELEMENT precence
    def wait_for_element_precense(self, locator):
        try:
            WebDriverWait(self.driver, 30).until((EC.presence_of_element_located(locator)))
        except TimeoutException:
            print("it took so long to load")

    '''
        ===========================================================================
        ===========================================================================
        Methods of Browser Helper
        ===========================================================================
        ===========================================================================
    '''

    '''
        capture image, pass value to name an image
        capture is flash, so need to pass locator for visible to capture more exactly, if not capture maybe not expectation.
    '''
    def screenshot(self, name, locator=None):
        try:
            if locator is not None:
                self.wait_for_element_visible(locator)
            allure.attach(self.driver.get_screenshot_as_png(), name=name,
                          attachment_type=allure.attachment_type.PNG)
        except Exception as e:
            print(e)


    '''
        ===========================================================================
        ===========================================================================
        Methods related execute script
        ===========================================================================
        ===========================================================================
    '''

    # scroll to element using JavaScript
    def move_to_element(self, locator):
        try:
            self.wait_for_element_visible(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", self.driver.find_element(*locator))
        except Exception as e:
            print(e)

    #    Open new tab
    def open_new_tab(self):
        self.driver.execute_script("window.open('');")

    #    move/ switch to indexed tab, default current tab is 0
    def switch_tab(self, index):
        self.driver.switch_to.window(self.driver.window_handles[index])


    # some instance, element not visible or tricky to click, let take execute execute script
    def click_element_script(self, locator):
        try:
            self.wait_for_element_precense(locator)
            s = self.driver.find_element(locator)
            self.driver.execute_script("arguments[0].click();", s)
        except Exception as e:
            print(e)

    '''
        ===========================================================================
        Manage cookies
        ===========================================================================
    '''

    # add new cookie
    def add_cookie(self, name, value):
        self.driver.add_cookie({"name": name, "value": value})

    # get cookie
    def get_cookie(self, name=""):
        if name == "":
            return self.driver.get_cookies()
        else:
            return self.driver.get_cookie(name)

    # delete cookie
    def delete_cookie(self, name=""):
        if name == "":
            self.driver.delete_all_cookies()
        else:
            self.driver.delete_cookie(name)

