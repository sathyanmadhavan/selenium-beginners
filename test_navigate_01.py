"""
This tutorial helps to navigate to a URL using selenium
"""
from selenium import webdriver

class page:
        def browser(self):
                self.browser = webdriver.Firefox()
                self.browser.get('https://edumarshal.com/')
                self.browser.quit()

class page_title():
        def title(self):   
                self.title = "Best School ERP Software | School Management Software | Edumarshal" 
                if self.title=="Best School ERP Software | School Management Software | Edumarshal":
                        print ("Success: Login page launched successfully")
                else:
                        print ("Failed: Login page Title is incorrect")

class facade():
        def __init__(self):
                self.site=page()
                self.begin=page_title()
        def begin_test(self):
                self.site.browser()
                self.begin.title()

if __name__ == "__main__":
        navigate=facade()
        navigate.begin_test()