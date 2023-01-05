"""
This tutorial will help to set the dropdown menu
"""
import time
from selenium import webdriver
class drop_down():
    def driver(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get("https://edumarshal.com/")
        dropdown_element = self.driver.find_element("xpath", "//li[@id='menu-item-2365']")
        dropdown_element.click()
        time.sleep(1)
        self.driver.find_element("xpath", "//span[text()='College ERP']").click()
        time.sleep(3)
        self.driver.close()

class client():
    def __init__(self):
        self.site=drop_down()
                
    def begin_test(self):
        self.site.driver()

if __name__ == "__main__":
        navigate=client()
        navigate.begin_test()