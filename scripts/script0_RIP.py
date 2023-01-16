from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv

current_date = str(date.today()) ##текущая дата
##открываем таблицу
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##ссылка на сайт
url_jivaya_voda1 = "https://xn--80aaepkoi5a5le.xn--p1ai/catalog/voda/voda_pitevaya_zhivaya_kaplya_19l/?oid=1136"

pages = requests.get(url_jivaya_voda1).text  ##делаем запрос на сайт, получаем html

soup = bs(pages, "lxml")        ##конвертируем полученный html в удобный формат

first = soup.find("div", class_ = "wraps hover_shine")       ##ищем на сайте необходимый элемент 
df.loc[0, current_date] = float(first.find("span", class_ = "price_value").text)  ##и записываем его в таблицу

df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
##сохраняем таблицу
