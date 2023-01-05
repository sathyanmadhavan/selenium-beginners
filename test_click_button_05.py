"""
Learn how to click a button in selenium
"""

import time
from selenium import webdriver
class click():
    def __init__(self):
# Create an instance of Chrome WebDriver
        self.driver = webdriver.Chrome()
    def test_click(self):
# Maximize the browser window
        self.driver.maximize_window()
# Navigate to  page
        self.driver.get("https://edumarshal.com/")

# KEY POINT: Locate the button and click on it
        button  = self.driver.find_element("xpath", "//input[@type='submit']")
        button.click()

# Pause the script to wait for page elements to load
        time.sleep(3)

# Close the browser
        self.driver.close()

click_test= click()
click_test.test_click()
