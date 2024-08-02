# import pytest
# from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
# from Utilities.readProperties import readConfig
# from selenium.webdriver.common.keys import Keys


class all_items:

    link_iqooZ9_partialLink = "Tornado Green"
    
    
    def __init__(self, driver) :
        self.driver=driver

    def clickProduct(self):
       
        iqooZ9_locator = (By.PARTIAL_LINK_TEXT, self.link_iqooZ9_partialLink)
        element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(iqooZ9_locator)
        )
        element.click()

        

        
        
