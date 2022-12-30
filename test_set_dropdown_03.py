"""
This tutorial will help to set the dropdown menu
"""
import time
from selenium import webdriver
def test_dropdown():
# Create an instance of Firefox WebDriver
    driver = webdriver.Firefox()
# Maximize the browser window
    driver.maximize_window()

# Navigate to  page
    driver.get("https://edumarshal.com/")

# KEY POINT: Identify the dropdown and click on it
    dropdown_element = driver.find_element("xpath", "//li[@id='menu-item-2365']")
    dropdown_element.click()
# Sleep is one way to pause while the page elements load
    time.sleep(1)

# KEY POINT: Locate a particular option and click on it
    driver.find_element("xpath", "//span[text()='College ERP']").click()
# Future tutorials cover explicit, implicit and ajax waits
    time.sleep(3)

# Close the browser window
    driver.close()
