from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from requests_html import HTMLSession

current_date = str(date.today()) ##текущая дата
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем таблицу
session = HTMLSession() ##создаем "сессию"

r = session.get("https://chebistok.ru") ##делаем запрос на сайт

soup = bs(r.html.html, "lxml") ##преобразуем полученный html в удобный формат
first = soup.find("section", class_ = "product")
second = first.find("p", class_ = "smal").text.split('=', 1)[1].lstrip()
third = first.find("p", class_ = "price green").text ##ищем элементы и записываем в таблицу

df.loc[14, current_date] = float(''.join([i for i in second if i.isdigit()]))
df.loc[15, current_date] = float(''.join([i for i in third if i.isdigit()]))
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')

