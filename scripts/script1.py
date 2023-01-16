from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By ##все для selenium
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time ##для sleep

current_date = str(date.today()) ##текущая дата
options = Options()
#options.add_argument("--headless")
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir=C:/Users/Kirill/Desktop/profiles')
options.add_argument('--profile-directory=Profile 1') 

browser = webdriver.Chrome(options=options) ##открываем браузер
browser.set_window_size(1051, 806) ##размер окна браузера
##открываем таблицу
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем сайт

browser.get("https://живаякапля.рф/catalog/water/water_drinking_zhivaya_kaplya_19l/?oid=1026")
time.sleep(3) ##время на загрузку элементов сайта
try:
    button1 = browser.find_element("xpath", '//*[@id="main"]/div[28]/div/div[2]/span[1]')
    button1.click() ##закрываем рекламу (если есть)
except Exception:
    pass
time.sleep(1)
button2 = browser.find_element("xpath", '//*[@id="bx_117848907_1012_prop_842_list"]/li[3]/span/span')
button2.click() ##находим и нажимаем нужную кнопку
time.sleep(1)
button3 = browser.find_element("xpath", '//*[@id="bx_117848907_1012_basket_actions"]/a')
button3.click()
time.sleep(2)
##находим элемент с ценой
price2 = browser.find_element("xpath", '//*[@id="basket-item-price-337"]').text
time.sleep(1)
price1 = browser.find_element("xpath", '//*[@id="basket-item-price-339"]').text

df.loc[0, current_date] = float(''.join([i for i in price1 if i.isdigit()]))
df.loc[1, current_date] = float(''.join([i for i in price2 if i.isdigit()]))
##записываем цену в таблицу и сохраняем
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
