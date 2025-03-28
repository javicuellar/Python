from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup



# The site we will scrape
website='https://www.scrapethissite.com/'

# Set up Chrome options
chrome_options = Options()
# Run Chrome in headless mode, without a UI or display server dependencies
chrome_options.add_argument("--headless")
# Disable the Chrome sandbox, useful in a containerized environment
chrome_options.add_argument("--no-sandbox")
# Overcome limited resource problems
chrome_options.add_argument("--disable-dev-shm-usage")

# Set up WebDriver with the specified Chrome options
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the webpage
driver.get(website)  
# Parse the page source with BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser') 

# Extract and print the page title
print('################ Thie title of the website is #################')
print(soup.find('title').text)

 # Close the browser
driver.quit() 