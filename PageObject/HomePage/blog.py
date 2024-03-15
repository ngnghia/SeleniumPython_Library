from Library.Commons import CommonMethods
from selenium.webdriver.common.by import By


class Blog(CommonMethods):

    def __init__(self, driver):
        self.driver = driver

    # element of "Simple Login Page"
    form_login = (By.NAME, "login")
    txt_username = (By.NAME, "userid")
    txt_password = (By.NAME, "pswrd")
    btn_login = (By.XPATH, "*//form[@name='login']/input[3]")
    btn_cancel = (By.XPATH, "*//form[@name='login']/input[4]")

    # element of table
    table = (By.ID, "table1")
    table_row = (By.XPATH, "*//table[@id='table1']/tbody/tr")

    # iframe
    frame1 = (By.ID, "iframe1")
    frame2 = (By.XPATH, "*//iframe[@id='iframe1']")

    # radio & check box
    radio1 = (By.ID, "radio1")
    radio2 = (By.ID, "radio2")

    chbox1 = (By.ID, "checkbox1")
    chbox2 = (By.ID, "checkbox2")

    link_dup_click = (By.ID, "testdoubleclick")
    droplist_delay = (By.XPATH, "*//div[@id='myDropdown']")
    btn_dropbtn    = (By.CLASS_NAME, "dropbtn")

    # Select multi item
    select = (By.ID, "multiselect1")

    # Select multi item
    droplist = (By.ID, "drop1")

    # link open tab
    link_SeleniumTutorial = (By.XPATH, "*//a[@id='link2']")

    # button enable and disabled
    btn2_button = (By.ID, "but2")
    btn1_button = (By.ID, "but1")

    # textbox is disabled
    txt_tb2 = (By.ID, "tb2")

    #Ordered List
    order_list      = (By.XPATH, ("*//ol/li"))
    unorder_list    = (By.XPATH, ("*//ul/li"))

    # popup
    link_popup      = (By.LINK_TEXT, "Open a popup window")

    # upload file
    # btn_upload_file = (By.ID, "uploadfile")
    btn_upload_file = (By.XPATH, "*//input[@type='file']")
    # btn_upload_file = (By.XPATH, "*//form[@action='demo_form.asp']/input")

    ''' ======================================
    Testing METHODS on this page
    ======================================'''

    # loop and print each cell text in  table.
    def read_table_data(self):
        for i in range(1, len(self.get_element_list(self.table_row)) + 1):
            row = []
            for j in range(1, 4):
                row.append(self.driver.find_element(*(By.XPATH, "*//table[@id='table1']/tbody/tr[%s]/td[%s]" % (i, j))).text)
            print(row)

    # read data droplist, orderlist..
    def read_data_droplist(self):
        for i in self.get_element_list(self.order_list):
            print(i.text)