from selenium.webdriver.common.by import By
from Library.Commons import CommonMethods

class Home(CommonMethods):

    def __init__(self, driver):
        self.driver = driver

    inventory           = (By.ID, "inventory_container")
    list_product        = (By.XPATH, "*//div[@class='inventory_list']/div")
    productname    = "*//div[@class='inventory_list']/div[%s]/div[2]/div[1]/a/div"
    productprice   = "*//div[@class='inventory_list']/div[%s]/div[2]/div[2]/div"
    btn_addtocart  =  "*//div[@class='inventory_list']/div[%s]/div[2]/div[2]/button"
    cart_link           = (By.CSS_SELECTOR, ".shopping_cart_link")

    # loop items, if match name, click add to cart.
    def select_product_by_name(self, name):
        for i in range(1, len(self.get_element_list(self.list_product)) + 1):
            if self.driver.find_element(*(By.XPATH, self.productname % i)).text.lower().strip() == name.lower().strip():
                self.driver.find_element(*(By.XPATH, self.btn_addtocart % i)).click()
                break