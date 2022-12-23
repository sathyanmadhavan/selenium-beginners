from selenium import webdriver

# Create an instance of Firefox WebDriver
browser = webdriver.Firefox()

# KEY POINT: The driver.get method will navigate to a page given by the URL
browser.get('https://edumarshal.com/?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxYzQa8u5bjYvZ8gMpm43uXkWXovhfRqJp7TaInW6ebpPpQi73XzhDhoCEhoQAvD_BwE')

# Check if the title of the page is proper
if(browser.title=="Best School ERP Software | School Management Software | Edumarshal"):
    print ("Success: Login page launched successfully")
else:
    print ("Failed: Login page Title is incorrect")

# Quit the browser window
browser.quit()
