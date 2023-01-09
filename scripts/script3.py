from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv

current_date = str(date.today()) ##текущая дата
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем таблицу
#################################
##Горный оазис, 2 штуки (одну нельзя)
url_gornaya = "https://www.74mv.ru/katalog/gornyj-oazis" ##ссылка на сайт
pages = requests.get(url_gornaya).text ##получаем html

soup = bs(pages, "lxml")  ##преобразуем в нужный формат                        

first = soup.find("div", class_ = "wrapper") ##ищем элемент и записываем в таблицу
df.loc[4, current_date] = float(first.find("span", class_ = "PriceunitPrice").text.split(',')[0])
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
