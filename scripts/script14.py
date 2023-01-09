from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options ##всё для selenium
from selenium.webdriver.common.action_chains import ActionChains
import time

current_date = str(date.today()) ##текущая дата
options = Options() 
options.add_argument("--headless") ##параметр, чтоб браузер не открывался явно

browser = webdriver.Chrome(options=options) ##открываем браузер
##открываем таблицу
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')

browser.get("https://l-w.ru/catalog/voda/voda_19l/") ##открываем сайт
browser.set_window_size(1051, 806) ##размер окна
time.sleep(2)
try:
    ActionChains(browser).move_by_offset(800, 150).click().perform()
    time.sleep(2) ##закрываем рекламу (клик)
except Exception:
    pass ##если не кликается, то идем дальше
##находим элемент с ценой за 1 шт
price1 = browser.find_element("xpath", '//*[@id="content"]/div/div/div/div[2]/div[1]/div[1]/div[2]').text
##находим и жмем кнопку, чтоб появилась цена за 2 шт
button1 = browser.find_element("xpath", '//*[@id="content"]/div/div/div/div[2]/div[1]/div[2]/button[2]')
button1.click()
time.sleep(1)
##находим элемент с ценой за 2шт и записываем все в таблицу
price2 = browser.find_element("xpath", '//*[@id="content"]/div/div/div/div[2]/div[1]/div[1]/div[2]').text
df.loc[22, current_date] = float(''.join([i for i in price1 if i.isdigit()]))
df.loc[23, current_date] = float(''.join([i for i in price2 if i.isdigit()]))
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
