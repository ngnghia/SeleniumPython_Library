from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Library.Commons import CommonMethods


class Home(CommonMethods):

    def __init__(self, driver):
        self.driver = driver

    txt_search = (By.NAME, 'q')
    list_search_suggest = (By.XPATH, "*//ul/li[@class='_3D0G9a']")
    list_filter = (By.XPATH, "*//div[@class='_10UF8M']")
    list_product = (By.XPATH, "*//div[@class='_4rR01T']")
    # SELECT 1 item from suggestion when typing, need a argument.
    def select_suggest(self, value):
        self.wait_for_element_visible(self.list_search_suggest)
        list = self.driver.find_elements(*self.list_search_suggest)

        for item in list:
            if item.text.lower().replace('in mobiles', '').strip() == value.strip().lower():
                item.click()
                break

    def select_filter(self, category):
        self.wait_for_element_visible(self.list_filter)
        list = self.driver.find_elements(*self.list_filter)
        for item in list:
            if item.text.strip().lower() == category.strip().lower():
                item.click()
                break

    def select_product(self):
        list = self.driver.find_elements(*self.list_product)
        i = 0
        for item in list:
            if i == 0:
                item.click()
                break

    def wait_for_element_presence(self, locator):
        try:
            WebDriverWait(self.driver, 30).until((EC.presence_of_element_located(locator)))
        except TimeoutException:
            print("it took so long to load")

    def wait_for_element_visible(self, locator):
        try:
            WebDriverWait(self.driver, 30).until((EC.visibility_of_all_elements_located(locator)))
        except TimeoutException:
            print("it took so long to load")
