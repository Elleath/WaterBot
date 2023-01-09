from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv

current_date = str(date.today()) ##текущая дата
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем таблицу
####################################
##Лидер (сайт заказчика) 
url_lider = "https://artvod.ru/catalog/lider19-2/" ##ссылка на сайт
pages = requests.get(url_lider).text ##получаем html

soup = bs(pages, "lxml")          ##преобразуем в нужный формат                 

first = soup.find("div", class_ = "body-inner")
second = first.find("div", class_ = "tovar_opisanie")
third = second.find_all("td")[2].text
four = second.find_all("td")[5].text  ##ищем цены и записываем в таблицу
df.loc[5, current_date] = float(''.join([i for i in third if i.isdigit()]))
df.loc[6, current_date] = float(''.join([i for i in four if i.isdigit()]))
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
