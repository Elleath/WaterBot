from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time
fdsfdsf ПОЧИНИТЬ ПОТОМ
current_date = str(date.today())
options = Options()
#options.add_argument("--headless") 

browser = webdriver.Chrome(options=options)
browser.set_window_size(1051, 806)

#df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

browser.get("https://niagara74.ru")
time.sleep(2)
try:
    button1 = browser.find_element("xpath", '//*[@id="acceptCookie"]')
    button1.click()
    time.sleep(1)
except Exception:
    pass
button2 = browser.find_element("xpath", '//*[@id="reverse-down"]')
button2.click()
time.sleep(5)
tara = browser.find_element("xpath", '//*[@id="basket-item-11411189"]/div/div[3]/div').text
print(tara)
#df.loc[7, current_date] = float(''.join([i for i in tara if i.isdigit()]))

#df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')

