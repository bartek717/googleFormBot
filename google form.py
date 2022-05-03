import time
from selenium import webdriver
import smtplib
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

browser = "C:\webdrivers/chromedriver"
s = Service(browser)

options = Options()
options.add_argument("--incognito")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("window-size=1200x600")
driver = webdriver.Chrome(service=s)
form = "PUT LINK HERE" # put form here


iterations = 0

while iterations<3:
    try:
        driver.get(form)
        time.sleep(3)
        iterations+=1
        # def would need to change xpath to correct if you are using this
        cart = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[15]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div")
        #cart.click()
        time.sleep(1)
        second = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[2]/div[22]/div/div/div[2]/div[1]/div/span/div/div[3]/label/div/div[1]/div/div[3]/div")
        #second.click()
        time.sleep(1)
        submit = driver.find_element(By.XPATH, "/html/body/div/div[2]/form/div[2]/div/div[3]/div/div[1]/div/span/span")
        submit.click()
        iterations += 1
        restart = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")

    except:
        print("ERROR CAUGHT")
