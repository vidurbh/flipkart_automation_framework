import pytest
from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Utilities.readProperties import readConfig
from selenium.webdriver.common.keys import Keys


class add_items:

    input_search_xpath="//input[@placeholder='Search for Products, Brands and More']"
    
    def __init__(self, driver) :
        self.driver=driver

    def setProduct(self, product):
        # print("product name set to ", product)
        self.driver.find_element(By.XPATH, self.input_search_xpath).clear()
        if product:
            self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(product)
            self.driver.find_element(By.XPATH, self.input_search_xpath).send_keys(Keys.ENTER)            
        else:
            print("product is not given")
        
