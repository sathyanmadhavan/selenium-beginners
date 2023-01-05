"""
This test helps to fill the text
"""
import time
from selenium import webdriver
class page_values():
    def driver(self):
        self.driver = webdriver.Firefox()
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
        time.sleep(3)
        self.driver.quit()

class client():
     def __init__(self):
                self.site=page_values()
                
     def begin_test(self):
                self.site.driver()

if __name__ == "__main__":
        navigate=client()
        navigate.begin_test()
