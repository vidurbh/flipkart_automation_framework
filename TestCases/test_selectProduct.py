import time
import selenium
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from PageObjects.flipkarthomepage import add_items
from PageObjects.allproductpage import all_items
from PageObjects.desiredproductpage import actual_product_page
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class TestProdSearch:
    baseURL=readConfig.getURL().strip()
    pageTitle=readConfig.getMainPageTitle().strip()
    item=readConfig.getProductName()
    productURL=readConfig.getProductURL().strip()
    # print("product url", productURL)
    logger=LogGen.loggen()


    def test_selectProduct(self, setup):
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        itemObject=add_items(self.driver)
        itemObject.setProduct(self.item)
        desiredProduct=all_items(self.driver)
        desiredProduct.clickProduct()
        time.sleep(2)
        self.windows=self.driver.window_handles
        # print("all window handles", len(self.windows))
        self.new_window=self.windows[1]
        self.driver.switch_to.window(self.new_window)
        app=actual_product_page(self.driver)
        
        try:
            app.is_addToCart()
            self.logger.info("Test Case Passed")
            self.driver.quit()
            assert True

        except:
            self.logger.info("Test Case Failed")
            self.driver.quit()
            assert False


            
        
        