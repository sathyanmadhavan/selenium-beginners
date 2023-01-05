"""
Learn to count the rows in a table using Selenium
"""
import time
from selenium import webdriver
class count_rows():
    def __init__(self):
# Create an instance of Firefox WebDriver
        self.driver = webdriver.Firefox()
# Maximize the browser window
    def test_count_rows(self):
        self.driver.maximize_window()
# Navigate to page
        self.driver.get("https://statisticstimes.com/sports/ipl/all-ipl-points-table.php")

# Find the table element in the page
        table = self.driver.find_element("xpath", "//table[@id='table_main']")

# KEY POINT: Find the tr elements in the table
        rows = table.find_elements("xpath", "//tbody/descendant::tr")


        print("Total No of Rows: %d" %len(rows))

# Pause the script for 3 seconds
        time.sleep(3)

# Close the browser
        self.driver.close()

rows= count_rows()
rows.test_count_rows()