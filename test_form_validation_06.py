"""
Check for the presence of absence of page elements
"""
import time
from selenium import webdriver
def test_form_validation():
# Create an instance of IE WebDriver
    driver = webdriver.Firefox()
# Maximize the browser window
    driver.maximize_window()
# Navigate to Qxf2 Tutorial page
    driver.get("https://edumarshal.com/")

# Find the  button and click it
    button = driver.find_element("xpath" ,"//input[@type='submit']")
    button.click()
# Pause the script to wait for validation messages to load
    time.sleep(3)
# KEY POINT: Check if the validation mesage for name field
    try:
        driver.find_element("xpath", "//div[text()='This field is required.']")
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
    driver.close()
