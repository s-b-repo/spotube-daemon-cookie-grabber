from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# URL to open
url = 'http://example.com'

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("window-size=1,1")

# Set up Chrome driver
service = Service('/usr/bin/chromedriver')
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open the URL
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Grab the cookie
cookies = driver.get_cookies()
for cookie in cookies:
    if cookie['name'] == 'dc_cookie':
        print(f"dc_cookie: {cookie['value']}")

# Clean up
driver.quit()
