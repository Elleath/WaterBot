from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time

current_date = str(date.today())
options = Options()
options.add_argument("--headless") 

browser = webdriver.Chrome(options=options)
browser.set_window_size(1051, 806)

df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

browser.get("https://voda174.ru")
time.sleep(2)
browser.execute_script("window.scrollTo(0, 900)")
time.sleep(1)

button1 = browser.find_element("xpath", '//*[@id="5f97f35effcd48f0bc1d8416f1e6f684"]/div/div/a')
button1.click()
time.sleep(1)
tara = browser.find_element("xpath", '//*[@id="f75f5656e56542c78645cf2ff4fe6b05"]/div/b').text

df.loc[1, current_date] = float(''.join([i for i in tara if i.isdigit()]))

df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')

