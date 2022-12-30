"""
Learn to hover over elements using Selenium
"""
import time
from selenium import webdriver

#Notice this extra import statement!
from selenium.webdriver.common.action_chains import ActionChains
def test_hover():
# Create an instance of Firefox WebDriver
    driver = webdriver.Firefox()
# Maximize the browser window
    driver.maximize_window()
# Navigate to  page
    driver.get("https://edumarshal.com/")
# Locate the Resource element to hover over
    resource = driver.find_element("xpath", "//li[@id='menu-item-2576']")
# KEY POINT: Use ActionChains to hover over elements
    action = ActionChains(driver)
    action.move_to_element(resource)
    action.perform()
    time.sleep(3) #Adding waits to make the example more visual
    attendance = driver.find_element("xpath", "//span[text()='Attendance Tracking']")
    attendance.click()
    time.sleep(3)
# Close the browser
    driver.close()
