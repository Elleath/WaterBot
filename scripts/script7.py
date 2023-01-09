from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv

current_date = str(date.today()) ##текущая дата
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем таблицу
###########################
##Артенза
url_artenza = "https://arkhiz74.ru/page/19litrov/" ##ссылка на сайт
pages = requests.get(url_artenza).text   ##получаем html

soup = bs(pages, "lxml")  ##преобразуем в нужный формат                        

first = soup.find("body", class_ = "") #ищем элементы и записываем в таблицу
second = first.find_all("span", style = "font-family: mceinline;")[22].text.strip()
third = first.find_all("span", style = "font-family: mceinline;")[23].text.strip()
df.loc[11, current_date] = float(''.join([i for i in second if i.isdigit()]))
df.loc[12, current_date] = float(''.join([i for i in third if i.isdigit()]))
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
