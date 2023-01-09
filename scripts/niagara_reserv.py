from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")

browser = webdriver.Chrome(options=options)

browser.get("https://niagara74.ru")
time.sleep(20)
button1 = browser.find_element("xpath", '//*[@id="pp_24533"]/div[3]/div/div/div/a')
button2 = browser.find_element("xpath", '//*[@id="acceptCookie"]')
button3 = browser.find_element("xpath", '//*[@id="bx_1970176138_401_0564dce275e0399e557aae3bf75c32cd_buy_link"]')
button1.click()
time.sleep(1)
button2.click()
time.sleep(1)
button3.click()
time.sleep(3)

niagpr2 = browser.find_element("xpath", '//*[@id="bx_1970176138_385_f5e07bd0ab70548a3db9e6f096af74cd_price"]').text
niagpr1 = browser.find_element("xpath", '//*[@id="bx_1970176138_385_f5e07bd0ab70548a3db9e6f096af74cd_price_old"]').text
niag2 = browser.find_element("xpath", '//*[@id="bx_1970176138_401_0564dce275e0399e557aae3bf75c32cd_price"]').text
niag1 = browser.find_element("xpath", '//*[@id="bx_1970176138_401_0564dce275e0399e557aae3bf75c32cd_price_old"]').text

print(niagpr2)
print(niagpr1)
print(niag2)
print(niag1)


