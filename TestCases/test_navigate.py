import selenium
from Utilities.readProperties import readConfig
from Utilities.customLogger import LogGen
from PageObjects.flipkarthomepage import add_items
from PageObjects.allproductpage import all_items
# from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



class TestNavigate:
        
        baseURL=readConfig.getURL().strip()
        pageTitle=readConfig.getMainPageTitle().strip()
        logger=LogGen.loggen()
     

        def test_navigateToFlipkart(self, setup):
                self.driver=setup
                self.driver.get(self.baseURL)
                self.driver.maximize_window()
                title=self.driver.title
                if title==self.pageTitle:
                    self.logger.info("Test Case Passed")
                    self.driver.quit()
                    assert True

                else :
                    self.logger.info("Test Case Failed")
                    self.driver.quit()
                    assert False