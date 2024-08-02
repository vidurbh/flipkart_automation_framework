import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utilities.readProperties import readConfig
from selenium.webdriver.common.keys import Keys
from Utilities.customLogger import LogGen


class actual_product_page:
    logger=LogGen.loggen()
    button_addToCart_xpath="//button[@class='QqFHMw vslbG+ In9uk2']"
    
    def __init__(self, driver) :
        self.driver=driver

    def is_addToCart(self):


        addtocart = (By.XPATH, self.button_addToCart_xpath)
        
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(addtocart))
            return True 

        except:
            return False
        
    def click_addToCart(self):
        addtocart = (By.XPATH, self.button_addToCart_xpath)        
        try:
            # element=WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(addtocart))
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(addtocart)).click()

            time.sleep(5)
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            # element.click() 
            print("button clicked addtocart")
            # self.logger.info(f"Button is enabled: {element.is_enabled()}")
        except Exception as e:
            self.logger.error(f"Unable to locate or click add to cart button: {str(e)}")
            return False







        

        
        
