from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains ## MAYBE
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from random import randint, randrange
import time 
import random
import winsound

AMAZON_URL = 'https://www.amazon.it/Playstation-Sony-PlayStation-5/dp/B08KKJ37F7'
WAIT_TIME = 5
PRICE_LIMIT = 700.00
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver=webdriver.Chrome(PATH)
driver.get(AMAZON_URL)
button0 = driver.find_element_by_id("nav-link-accountList")
button = driver.find_element_by_id('nav-flyout-ya-signin')
ActionChains(driver).move_to_element(button0).perform()
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(button).click(button).perform()
driver.implicitly_wait(10)
mail = driver.find_element_by_id("ap_email")
mail.send_keys("mailmail@mail.com") #insert mail
mail.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
pwd = driver.find_element_by_id("ap_password")
pwd.send_keys("pwdpwdpwd") #insert pwd
pwd.send_keys(Keys.RETURN)
driver.implicitly_wait(10)
available = driver.find_element_by_class_name('a-color-price').text
s=str(available)
driver.implicitly_wait(10)
conto = 0
while s== "Non disponibile.":
    driver.implicitly_wait(10)
    driver.refresh()
    conto+=1
    print(conto)
    driver.implicitly_wait(10)
    available = driver.find_element_by_class_name('a-color-price').text
    s=str(available)

print('++++PS5 DISPONIBILE!!!!++++')
button2 = driver.find_element_by_id('buy-now-button')
driver.implicitly_wait(10)
ActionChains(driver).move_to_element(button2).click(button2).perform() 
