from selenium  import webdriver
import time


driver = webdriver.Chrome()

url = "https://github.com/emreekinci"
driver.get(url)

time.sleep(2)
driver.maximize_window()

if "emreekinci" in driver.title:
    driver.save_screenshot("github.com-emreekinci.png") #  Capture the screenshot of the page
    
print(driver.title)
time.sleep(3)

url2 = "https://github.com"
driver.get(url2)
driver.save_screenshot("github.com-homepage.png") #  Capture the screenshot of the page


print(driver.title)
time.sleep(2)
driver.back() #  Go back to previous page (To go forward use driver.forward())
driver.forward()  
time.sleep(2)

driver.close
