"""
Learn to count the rows in a table using Selenium
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to page
driver.get("https://statisticstimes.com/sports/ipl/all-ipl-points-table.php")

# Find the table element in the page
table = driver.find_element("xpath", "//table[@id='table_main']")

# KEY POINT: Find the tr elements in the table
rows = table.find_elements("xpath", "//tbody/descendant::tr")


print("Total No of Rows: %d" %len(rows))

# Pause the script for 3 seconds
time.sleep(3)

# Close the browser
driver.close()
