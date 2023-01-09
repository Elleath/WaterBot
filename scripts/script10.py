from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from requests_html import HTMLSession

current_date = str(date.today()) ##текущая дата
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
session = HTMLSession() ##открываем таблицу и создаем "сессию"
##получаем данные с сайта
r = session.get("https://niagara74.ru/catalog/pitevaya_voda/19_l_niagara_premium_pit_voda/")

soup = bs(r.html.html, "lxml") ##преобразуем в удобный формат
first = soup.find("div", class_ = "middle") ##ищем элементы и записываем их в таблицу
second = first.find("div", class_ = "product-item-detail-price-current").text.strip()
third = first.find("div", class_ = "product-item-detail-price-old").text.strip()
df.loc[17, current_date] = float(''.join([i for i in second if i.isdigit()]))
df.loc[16, current_date] = float(''.join([i for i in third if i.isdigit()]))
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
