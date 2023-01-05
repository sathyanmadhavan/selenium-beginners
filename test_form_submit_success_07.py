"""
Learn to fill and submit a form with Selenium
"""
import time
from selenium import webdriver

class form_submit():
    def __init__(self):
# Create an instance of Firefox WebDriver
        self.driver = webdriver.Firefox()
    def test_form_submit(self):
# Maximize the browser window
        self.driver.maximize_window()
        self.driver.get("https://edumarshal.com/")
        name=self.driver.find_element("xpath","//input[@name='input_1.3']")
        name.send_keys("Sathyan")
        name=self.driver.find_element("xpath","//input[@name='input_1.6']")
        name.send_keys("Madhavan")
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
        submit=self.driver.find_element("xpath","//input[@type='submit']")
        submit.click()

# Wait for the new page to load
        time.sleep(3)
    
        if self.driver.current_url== 'https://edumarshal.com/':
            print("Success")
        else:
            print("Failure")

# Close the browser
        self. driver.close()

submit_success= form_submit()
submit_success.test_form_submit()
