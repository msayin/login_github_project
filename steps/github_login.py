from selenium import webdriver

import time

browser = webdriver.Chrome()

browser.get("https://www.github.com")

time.sleep(5)
Signin = browser.find_element_by_xpath("/html/body/div[1]/header/div/div[2]/div[2]/a[1]")
Signin.click()
time.sleep(5)

login = browser.find_element_by_name("login")
password = browser.find_element_by_name("password")

login.send_keys("xxxxxx")
password.send_keys("@xxxxx@")

time.sleep(5)

login = browser.find_element_by_xpath("//*[@id='login']/form/div[3]/input[8]")
login.click()
time.sleep(10)

browser.close()

