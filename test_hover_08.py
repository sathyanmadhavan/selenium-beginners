"""
Learn to hover over elements using Selenium
"""
import time
from selenium import webdriver
#Notice this extra import statement!
from selenium.webdriver.common.action_chains import ActionChains
class hover():
    def __init__(self):
# Create an instance of Firefox WebDriver
        self.driver = webdriver.Firefox()
    def test_hover(self):
# Maximize the browser window
        self.driver.maximize_window()
# Navigate to  page
        self.driver.get("https://edumarshal.com/")
# Locate the Resource element to hover over
        resource = self.driver.find_element("xpath", "//li[@id='menu-item-2576']")
# KEY POINT: Use ActionChains to hover over elements
        action = ActionChains(self.driver)
        action.move_to_element(resource)
        action.perform()
        time.sleep(3) #Adding waits to make the example more visual
        attendance = self.driver.find_element("xpath", "//span[text()='Attendance Tracking']")
        attendance.click()
        time.sleep(3)
# Close the browser
        self.driver.close()
test_hover=hover()
test_hover.test_hover()
