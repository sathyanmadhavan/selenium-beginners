"""
Selenium script that performs several common actions like:
click button, select dropdown, enable checkbox, set text
"""
import time
from selenium import webdriver
class consolidated():
    def __init__(self):
# Create an instance of Firefox WebDriver
        self.driver = webdriver.Firefox()
    def consolidated_test(self):
# Maximize the browser window
        self.driver.maximize_window()
        self.driver.get("https://edumarshal.com/")
        first_name=self.driver.find_element("xpath","//input[@name='input_1.3']")
        first_name.send_keys("Sathyan")
        last_name=self.driver.find_element("xpath","//input[@name='input_1.6']")
        last_name.send_keys("Madhavan")
        message=self.driver.find_element("xpath","//input[@type='email']")
        message.send_keys("xxx@gmail.com")
        phone=self.driver.find_element("xpath","//input[@type='tel']")
        phone.send_keys("1234567890")
        name=self.driver.find_element("xpath","//input[@name='input_5']")
        name.send_keys("Asan institute")
        city=self.driver.find_element("xpath","//input[@name='input_8']")
        city.send_keys("chennai")
        number=self.driver.find_element("xpath","//input[@name='input_7']")
        number.send_keys("10")
        check=self.driver.find_element("xpath","//label[@for='choice_1_6_1']")
        check.click()

# Take screenshot
        self.driver.save_screenshot('School_management.png')

# Identify the xpath for Click me button and click on it
        submit=self.driver.find_element("xpath","//input[@type='submit']")
        submit.click()

# Pause the script for 3 sec
        time.sleep(3)

# Verify user is taken to  redirect url
        if self.driver.current_url== 'https://edumarshal.com/':
            print("Success")
        else:
            print("Failure")

# Pause the script for 3 sec
        time.sleep(5)

# Close the browser
        self.driver.close()

cons = consolidated()
cons.consolidated_test()
