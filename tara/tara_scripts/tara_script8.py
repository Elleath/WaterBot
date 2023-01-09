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

browser.get("https://vk.com/market-181723874")
time.sleep(2)

button1 = browser.find_element("xpath", '//*[@id="market_item3345663"]/div/div[2]/a')
button1.click()
time.sleep(2)

tara = browser.find_element("xpath", '//*[@id="market_item_box"]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/div[2]/span').text
df.loc[8, current_date] = float(''.join([i for i in tara if i.isdigit()]))

df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')


