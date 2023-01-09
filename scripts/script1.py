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
options.add_argument("--headless") ##опция, чтобы браузер не открывался в явном виде

browser = webdriver.Chrome(options=options) ##открываем браузер
browser.set_window_size(1051, 806) ##размер окна браузера
##открываем таблицу
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем сайт
browser.get("https://xn--80aaepkoi5a5le.xn--p1ai/catalog/voda/voda_pitevaya_zhivaya_kaplya_19l/?oid=1139")
time.sleep(3) ##время на загрузку элементов сайта
try:
    button1 = browser.find_element("xpath", '//*[@id="main"]/div[28]/div/div[2]/span[1]')
    button1.click() ##закрываем рекламу (если есть)
except Exception:
    pass
time.sleep(1)
button2 = browser.find_element("xpath", '//*[@id="bx_117848907_1067_prop_720_list"]/li[5]/span/span')
button2.click() ##находим и нажимаем нужную кнопку
time.sleep(2)
##находим элемент с ценой
price2 = browser.find_element("xpath", '//*[@id="content"]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[3]/div[1]/div[1]/div[1]/span[1]').text
df.loc[1, current_date] = float(''.join([i for i in price2 if i.isdigit()]))
##записываем цену в таблицу и сохраняем
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
