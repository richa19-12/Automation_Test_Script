from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time

# Set the path to the chromedriver executable
driver_path = r"C:\Users\Dell\Downloads\Compressed\chromedriver_win32_3\chromedriver.exe"

# Create a new Service instance
service = Service(executable_path=driver_path)

# Create a new Chrome webdriver instance using the Service object
driver = webdriver.Chrome(service=service)

# Navigate to Google.com
driver.get("https://www.google.com")

# Find the search box element by name and type a search query
search_box = driver.find_element(By.NAME,"q")
search_box.send_keys("Techdome.io")

time.sleep(1.0)
search_box.send_keys(Keys.ENTER)

driver.close()



