"""
Learn to parse the text within each cell of a table
"""
import time
from selenium import webdriver

# Create an instance of Firefox WebDriver
driver = webdriver.Firefox()
# Maximize the browser window
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("https://www.indiatoday.in/live-score/t20-world-cup-points-table/2022/")

# KEY POINT: Logic to get the text in each cell of the table
# Find the Example table element in the page
table = driver.find_element("xpath", "//div[@class='pointsDataTable']")
# Use find_elements_by_xpath method to get the rows in the table
row = table.find_elements("xpath", "//tbody/descendant::tr")
# Create a list to store the text
result_data = []
# Go to each row and get the no of columns and the navigate to column
# Then get the text from each column
for i in enumerate(0,len(row)):
    # Find no of columns by getting the td elements in each row
    cols = enumerate[i].find_elements("tag name", "td")
    cols_data = []
    for j in enumerate(0,len(cols)):
        # Get the text of each field
        cols_data.append(cols[j].text.encode('utf-8'))
    result_data.append(cols_data)

# Print the result list
print(result_data)

# Pause the script for 3 sec
time.sleep(3)

# Close the browser
driver.close()
