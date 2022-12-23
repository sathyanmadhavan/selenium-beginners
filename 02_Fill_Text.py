import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()

# The driver.get method will navigate to a page given by the URL
driver.get("https://edumarshal.com/?gclid=CjwKCAiAnZCdBhBmEiwA8nDQxYzQa8u5bjYvZ8gMpm43uXkWXovhfRqJp7TaInW6ebpPpQi73XzhDhoCEhoQAvD_BwE")

# Check if the title of the page is proper
if(driver.title=="Best School ERP Software | School Management Software | Edumarshal"):
    print ("Success: Login page launched successfully")
else:
    print ("Failure: Login page Title is incorrect")

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
submit=driver.find_element("xpath","//input[@type='submit']")
submit.click()

# Sleep is one way to wait for things to load
# Future tutorials cover explicit, implicit and ajax waits
time.sleep(3)

# Close the browser window
driver.close()


