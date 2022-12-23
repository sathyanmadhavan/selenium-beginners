import time
from selenium import webdriver

# Create an instance of IE WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("https://edumarshal.com/?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxYzQa8u5bjYvZ8gMpm43uXkWXovhfRqJp7TaInW6ebpPpQi73XzhDhoCEhoQAvD_BwE")

# Find the  button and click it
button  = driver.find_element("xpath" ,"//input[@type='submit']")
button.click()
# Pause the script to wait for validation messages to load
time.sleep(3)

# KEY POINT: Check if the validation mesage for name field
try:
    driver.find_element("xpath", "//div[text()='This field is required.']")
except Exception as e:
    #This pattern of catching all exceptions is ok when you are starting out
    result_flag = False
else:
    result_flag = True
if result_flag is True:
    print("Validation message for name present")
else:
    print("Validation message for name NOT present")

# Close the browser window
driver.close()
