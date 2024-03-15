import sys, os, time

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../../')
from Driver.driver import Driver
from PageObject.HomePage.home import Home

class TestHomePage(Driver):

    '''
    Demo script for search keyword,
    then select item from suggest list
    Select filter as ascending
    '''
    def test_search_product(self):
        home = Home(self.driver)

        # type keyword for searching
        home.input_textbox(home.txt_search, "iphone")
        home.screenshot("typing keywork")

        # get value from box
        print("inputted value is", home.get_value_textbox(home.txt_search))

        # select iphone 15 from suggested list
        home.select_suggest("iphone 15")
        home.screenshot("select item from suggested list")
        # filter ascending
        home.select_filter("Price -- Low to High")
        home.screenshot("after filter")

