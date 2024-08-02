import pytest
import selenium
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from PageObjects.flipkarthomepage import add_items
from PageObjects.allproductpage import all_items
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



import time




class TestProdSearch:
    baseURL=readConfig.getURL().strip()
    pageTitle=readConfig.getMainPageTitle().strip()
    item=readConfig.getProductName()
    logger=LogGen.loggen()
    product_page_URL=readConfig.getProductpageURL().strip()
    prodduct_page_title=readConfig.getProductpageTitle().strip()

    

    @pytest.mark.regression
    def test_prodsearch(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        itemObject=add_items(self.driver)
        itemObject.setProduct(self.item)
        current_title=self.driver.title.strip()
        print("Page title is ", current_title)
        print("Product page title is ", self.prodduct_page_title)
        print("current Page title length is ", len(current_title))
        print("Product page title is ", len(self.prodduct_page_title))
        if self.prodduct_page_title.lower() in current_title.lower():
            self.logger.info("****TEst case passed****")
            self.driver.quit()
            assert True
        else:
            self.logger.info("Test Case failed")
            self.driver.quit()
            assert False


    