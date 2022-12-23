import time
from selenium import webdriver
# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
driver.get("https://edumarshal.com/?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxYzQa8u5bjYvZ8gMpm43uXkWXovhfRqJp7TaInW6ebpPpQi73XzhDhoCEhoQAvD_BwE")
name=driver.find_element("xpath","//input[@name='input_1.3']")
name.send_keys("Sathyan")
name=driver.find_element("xpath","//input[@name='input_1.6']")
name.send_keys("Madhavan")
message=driver.find_element("xpath","//input[@type='email']")
message.send_keys("xxx@gmail.com")
phone=driver.find_element("xpath","//input[@type='tel']")
phone.send_keys("1234567890")
name=driver.find_element("xpath","//input[@name='input_5']")
name.send_keys("Asan institute")
city=driver.find_element("xpath","//input[@name='input_8']")
city.send_keys("chennai")
number=driver.find_element("xpath","//input[@name='input_7']")
number.send_keys("10")
check=driver.find_element("xpath","//label[@for='choice_1_6_1']").click()

# Take screenshot
driver.save_screenshot('D:\School_management.png')

# Identify the xpath for Click me button and click on it
submit=driver.find_element("xpath","//input[@type='submit']")
submit.click()

# Pause the script for 3 sec
time.sleep(3)

# Verify user is taken to Qxf2 tutorial redirect url
if (driver.current_url== 'https://edumarshal.com/?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxYzQa8u5bjYvZ8gMpm43uXkWXovhfRqJp7TaInW6ebpPpQi73XzhDhoCEhoQAvD_BwE'):
    print("Success")
else:
    print("Failure")

# Pause the script for 3 sec
time.sleep(5)

# Close the browser
driver.close()
