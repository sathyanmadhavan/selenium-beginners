"""
Check for the presence of absence of page elements
"""
import time
from selenium import webdriver
class form_validation():
    def __init__(self):
# Create an instance of IE WebDriver
        self.driver = webdriver.Firefox()
    def test_validation(self):
# Maximize the browser window
        self.driver.maximize_window()
# Navigate to Qxf2 Tutorial page
        self.driver.get("https://edumarshal.com/")

# Find the  button and click it
        button = self.driver.find_element("xpath" ,"//input[@type='submit']")
        button.click()
# Pause the script to wait for validation messages to load
        time.sleep(3)
# KEY POINT: Check if the validation mesage for name field
        try:
            self.driver.find_element("xpath", "//div[text()='This field is required.']")
        except RuntimeError as e:
    #This pattern of catching all exceptions is ok when you are starting out
            RESULT_FLAG = False
        else:
            RESULT_FLAG = True
        if RESULT_FLAG is True:
            print("Validation message for name present")
        else:
            print("Validation message for name NOT present")
# Close the browser window
        self.driver.close()
    
form_validation_test= form_validation()
form_validation_test.test_validation()
