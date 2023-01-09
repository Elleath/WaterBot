from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

current_date = str(date.today())
options = Options()
options.add_argument("--headless") 

browser = webdriver.Chrome(options=options)
browser.set_window_size(1051, 806)
df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

browser.get("https://l-w.ru/catalog/voda/voda_19l/")
time.sleep(2)
try:
    ActionChains(browser).move_by_offset(800, 150).click().perform()
    time.sleep(2)
except Exception:
    pass

button1 = browser.find_element("xpath", '//*[@id="content"]/div/div/div/div[2]/div[1]/a')
button1.click()
time.sleep(1)
browser.get("https://l-w.ru/personal/cart/")
time.sleep(2)
button2 = browser.find_element("xpath", '//*[@id="content"]/div/div[1]/div[1]/div/div[1]/div[3]/div[2]/div[2]/button[1]')
button2.click()
time.sleep(1)

tara = browser.find_element("xpath", '//*[@id="content"]/div/div[1]/div[1]/div/div[1]/div[5]/div[2]/div[2]/div[1]/span[2]').text
df.loc[9, current_date] = float(''.join([i for i in tara if i.isdigit()]))

df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')


