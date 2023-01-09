from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv

current_date = str(date.today())  ##текущая дата
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем таблицу
############################
##Любимая :)
headers = {              ##заголовок, чтобы сайт не распознал бота
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
  }
url_lubima = "https://vodalubima.ru" ##ссылка на сайт
pages = requests.get(url_lubima, headers=headers).text ##получаем html

soup = bs(pages, "lxml")     ##преобразуем в удобный формат                     

first = soup.find("div", id = "rec42533675")
second = first.find("div", class_ = "t776") ##ищем элемент и записываем в таблицу
df.loc[13, current_date] = float(second.find("div", class_ = "t776__price-value").text)
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
