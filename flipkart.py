from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import pytest

# Function to extract product details
def extract_product_details(driver):

    product_details = []
    for i in range(2 , 12,1):
        product_element_link = driver.find_element(By.CSS_SELECTOR , f'#container > div > div._36fx1h._6t1WkM._3HqJxg > div > div:nth-child(2) > div:nth-child({i}) > div > div > div > a')
        product_name = product_element_link.find_element(By.CSS_SELECTOR , 'div._4rR01T').text
        product_price = product_element_link.find_element(By.CSS_SELECTOR , 'div._30jeq3').text
        product_details.append({'Product Name': product_name, 'Display Price': product_price, 'Link to Product Details Page': product_element_link.get_attribute('href')})
    return product_details


browserstack_username = 'sahejjain_51cuxe'
browserstack_access_key = 'NDyQRRHYcFnCvGxZHqTW'

# Setting up Chrome WebDriver
desired_cap = {
      'resolution': '1024x768',
      'name': 'Flipkart Search Test',
      'build': 'Flipkart Search Test Build',
        'browser': 'Chrome',
        'browser_version': 'latest',
        'os': 'Windows',
        'os_version': '10',
      'browserstack.user': browserstack_username,
      'browserstack.key': browserstack_access_key
    }

    # Initialize the remote WebDriver
driver = webdriver.Remote(
    command_executor='http://'+browserstack_username+':'+browserstack_access_key+'@hub-cloud.browserstack.com/wd/hub',
    desired_capabilities=desired_cap
)

# Open Flipkart
driver.get("https://www.flipkart.com")
driver.maximize_window()

# # Close login popup if present
try:
    driver.find_element_by_xpath("//button[@class='_2KpZ6l _2doB4z']").click()
except:
    pass

# # Search for "Samsung Galaxy S10"
search_bar = driver.find_element("xpath", '//*[@id="container"]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
search_bar.send_keys("Samsung Galaxy S10")
search_bar.send_keys(Keys.RETURN)

time.sleep(3)
# # Click on "Mobiles" under Categories
mobiles_category = driver.find_element("xpath",'//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/div/section/div[3]/div/a')
mobiles_category.click()

time.sleep(3)


# # Apply Filters
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[3]/div[2]/div/div/div/label/div[1]'))).click()
time.sleep(3)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="container"]/div/div[3]/div[1]/div[1]/div/div[1]/div/section[4]/label/div[1]'))).click()
time.sleep(3)
# # Sort by Price: High to Low
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#container > div > div._36fx1h._6t1WkM._3HqJxg > div > div:nth-child(2) > div._1YokD2._2GoDe3.col-12-12 > div > div > div._5THWM1 > div:nth-child(5)'))).click()
time.sleep(3)
# # Extract and Print Product Details
product_details = extract_product_details(driver)
print()
print("Product Details:")
for product in product_details:
    print(product)
    print()

# # Close the WebDriver
driver.quit()
