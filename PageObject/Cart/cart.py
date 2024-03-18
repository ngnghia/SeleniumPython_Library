from selenium.webdriver.common.by import By
from Library.Commons import CommonMethods


class Cart(CommonMethods):

    def __init__(self, driver):
        self.driver = driver

    list_products = (By.XPATH, "*//div[@class='cart_item']")
    item_name          = (By.XPATH, "*//div[@class='cart_list']/div[%s]/div[2]/a/div")
    item_price          = (By.XPATH, "*//div[@class='cart_list']/div[%s]/div[2]/div[2]/div")
    btn_checkout        = (By.ID, "checkout")


    # def check_(self,):
    #     for i in range(1, len(self.get_element_list(self.list_products)) + 1):
    #         print("text", self.driver.find_element(
    #             *(By.XPATH, "*//div[@class='cart_list']/div[%s]/div[2]/a/div" % (i + 2))).text)
    #         print("price", self.driver.find_element(
    #             *(By.XPATH, "*//div[@class='cart_list']/div[%s]/div[2]/div[2]/div" % (i + 2))).text)

    # check product name, loop each row and compare price/name from param
    def check_product_detail(self, productdetail):
        flag = False
        try:
            for i in range(1, len(self.get_element_list(self.list_products)) + 1):
                name = self.driver.find_element(
                    *(By.XPATH, "*//div[@class='cart_list']/div[%s]/div[2]/a/div" % (i + 2))).text
                price = self.driver.find_element(
                    *(By.XPATH, "*//div[@class='cart_list']/div[%s]/div[2]/div[2]/div" % (i + 2))).text
                if productdetail['Name'].lower().strip() == name.lower().strip() and productdetail['Price'].lower().strip() == price.lower().strip():
                    flag = True
                    break
            return flag
        except Exception as e:
            print(e)


