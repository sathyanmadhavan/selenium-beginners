"""
This tutorial helps to navigate to a URL using selenium
"""
from selenium import webdriver

def test_title():

# Create an instance of Firefox WebDriver
        browser = webdriver.Firefox()

# KEY POINT: The driver.get method will navigate to a page given by the URL
        browser.get('https://edumarshal.com/')

# Check if the title of the page is proper
        test_title =="Best School ERP Software | School Management Software | Edumarshal"
        assert test_title == test_title
      

# Quit the browser window
        browser.quit()
