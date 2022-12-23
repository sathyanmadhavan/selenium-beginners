import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome("C:\chromedriver.exe")
# Maximize the browser window
driver.maximize_window()
# Navigate to  page
driver.get("https://edumarshal.com/?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxYzQa8u5bjYvZ8gMpm43uXkWXovhfRqJp7TaInW6ebpPpQi73XzhDhoCEhoQAvD_BwE")

# KEY POINT: Locate the button and click on it
button  = driver.find_element("xpath", "//input[@type='submit']")
button.click()

# Pause the script to wait for page elements to load
time.sleep(3)

# Close the browser
driver.close()

