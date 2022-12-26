"""
Learn how to click a button in selenium
"""

import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Navigate to  page
driver.get("https://edumarshal.com/")

# KEY POINT: Locate the button and click on it
button  = driver.find_element("xpath", "//input[@type='submit']")
button.click()

# Pause the script to wait for page elements to load
time.sleep(3)

# Close the browser
driver.close()
