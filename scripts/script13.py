from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait ##необходимо для selenium
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
import time ##для sleep

current_date = str(date.today()) ##текущая дата
options = Options()
options.add_argument("--headless") ##параметр, чтоб браузер не открывался явно

browser = webdriver.Chrome(options=options) ##открываем браузер
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')

browser.get("http://vlasovkluch.ru/cat/product/item_6.html") ##открываем сайт
time.sleep(2)
button1 = browser.find_element("xpath", '/html/body/div/div[1]/main/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div[2]/a')
##находим нужные кнопки и жмем
button1.click()
time.sleep(1)
browser.switch_to.alert.accept() ##принимаем предупреждение в браузере
time.sleep(2)
browser.refresh() ##обновляем сайт (чтоб цены появились)
##находим элемент и записываем в таблицу
vlasov = browser.find_element("xpath", '/html/body/div/div[1]/main/div/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div[1]/div[3]/div/div[1]').text
df.loc[20, current_date] = float(''.join([i for i in vlasov if i.isdigit()]))
df.loc[21, current_date] = float(''.join([i for i in vlasov if i.isdigit()]))
##сохраняем в таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
