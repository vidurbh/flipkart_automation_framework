from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utilities.readProperties import readConfig
from selenium.webdriver.common.keys import Keys


class actual_product_page:

    button_addToCart_xpath="//button[@class='QqFHMw vslbG+ In9uk2']"
    
    def __init__(self, driver) :
        self.driver=driver

    def is_addToCart(self):


        addtocart = (By.XPATH, self.button_addToCart_xpath)
        
        try:
            element = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(addtocart))
            return True 

        except:
            return False

        

        
        
