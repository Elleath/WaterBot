from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options ##все для selenium
from selenium.webdriver.common.action_chains import ActionChains
import time ##для sleep

current_date = str(date.today()) ##текущая дата
options = Options()
options.add_argument("--headless") ##параметр, чтоб браузер не открывался явно

browser = webdriver.Chrome(options=options) ##запускаем браузер
##открываем таблицу
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')

browser.get("https://niagara74.ru") ##открываем сайт
browser.set_window_size(1051, 806)  ##размер окна
time.sleep(20)           ##ждем 20 секунд, так как появляется реклама
try:
    ActionChains(browser).move_by_offset(800, 150).click().perform()
    time.sleep(2)  ##делаем клик, чтобы закрыть рекламу
except Exception:
    pass         ##если рекламы не появилось, то идем дальше

try:
    button1 = browser.find_element("xpath", '//*[@id="pp_24533"]/div[3]/div/div/div/a')
    button1.click() ##соглашаемся со сбором куки
except Exception:
    pass   ##если не надо, то идем дальше
button2 = browser.find_element("xpath", '//*[@id="acceptCookie"]') ##ищем нужные кнопки
button3 = browser.find_element("xpath", '//*[@id="bx_1970176138_401_f5e07bd0ab70548a3db9e6f096af74cd_buy_link"]')
#button1.click()
#time.sleep(1)
button2.click() ##нажимаем кнопки, чтобы появилась нужная цена
time.sleep(1)
button3.click()
time.sleep(3) ##задержка, чтобы данные успели подгрузиться
##находим нужный элемент и записываем в таблицу
niag2 = browser.find_element("xpath", '//*[@id="bx_1970176138_401_f5e07bd0ab70548a3db9e6f096af74cd_price"]').text
df.loc[19, current_date] = float(''.join([i for i in niag2 if i.isdigit()]))
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
