"""
Learn to select a checkbox using Selenium

"""
import time
from selenium import webdriver
# Create an instance of Firefox WebDriver
class Checkbox:
    def __init__(self):
        self.driver = webdriver.Firefox()
 
    def test_checkbox(self):
        # Maximize the browser window
        self.driver.maximize_window()
        self.driver.get("https://edumarshal.com/")
 
        check=self.driver.find_element("xpath","//label[@for='choice_1_6_1']")
        check.click()
 
        # Pause the script for 3 sec so you can confirm the check box was selected
        time.sleep(3)
 
        # Close the browser window
        self.driver.close()
 
# Create an instance of FacadeTestCheckbox
checkbox_test = Checkbox()
 
# Call the test_checkbox method
checkbox_test.test_checkbox()
