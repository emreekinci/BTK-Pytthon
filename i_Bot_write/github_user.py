from githubUserInfo import username, password
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time

class Github:
    def __init__(self, username, password):
        self.browser = webdriver.Chrome()
        self.username= username
        self.password = password
        #self.followers = []
        
    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2) #wait for page to load
        
        self.browser.find_element("xpath", "//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element("xpath", "//*[@id='password']").send_keys(self.password)
        # username.send_keys(self.username)
        # password.send_keys(self.password)
        time.sleep(10)
        #self.browser.find_element(By.XPATH, "//*[@id='login']/div[4]/form/div/font/font/input").click() # //*[@id="login"]/div[4]/form/div/font/font/input
        b = WebDriverWait(self.browser, 20).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="login"]/div[4]/form/div/font/font/input')))
        b.click()
        #self.browser.find_element_by_xpath("//*[@id='login']/div[4]/form/div/font/font/input").click() # old way of getting xpath
        #self.browser.find_element(By.XPATH, "//input[@id='login]").click() # //*[@id="login"]/div[4]/form/div/font/font/input  # //*[@id="login"]/div[4]/form/div/font/font/input
        #self.browser.find_element(by=By.XPATH, value='//*[@id="login"]/div[4]/form/div/font/font/input').click()

        #b = WebDriverWait(dr, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@class='ui fluid right labeled icon primary button' and contains(., 'Create download package')]")))
        #b = dr.find_element(By.XPATH, "//button[@class='ui fluid right labeled icon primary button' and contains(., 'Create download package')]")

    # def getFollowers(self):
    #     self.browser.get(f'https://github.com/{self.username}?tab=followers')
    #     time.sleep(2)
        
    #     items = self.browser.find_elements_by_css_selector(".d-table table-fixed")
    #     for i in items:
    #         self.followers.append(i.find_element_by_css_selector(".f4 Link--primary").text) 
        
github = Github(username, password) 
github.signIn()
# github.getFollowers()
# print(github.followers)


# https://github.com/SeleniumHQ/selenium/blob/a4995e2c096239b42c373f26498a6c9bb4f2b3e7/py/CHANGES

# https://stackoverflow.com/questions/72754651/attributeerror-webdriver-object-has-no-attribute-find-element-by-xpath

# from selenium.webdriver.common.by import By
# driver.find_element(by=By.XPATH, value='//<your xpath>')
