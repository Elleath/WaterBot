from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv

current_date = str(date.today()) ##текущая дата
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем таблицу
###########################
##кристальная, 1шт
url_krist1 = "https://voda174.ru/?ysclid=la432yrmmv765419697" ##сайт
pages = requests.get(url_krist1).text ##получаем html

soup = bs(pages, "lxml")  ##преобразуем в нужный вид                        

first = soup.find("body", class_ = "sprint5 margin-v2") ##находим необходимый элемент
second = first.find("div", class_ = "blk-data clearfix font-38").text.split('х')[1] ##split обрезает по знаку х
df.loc[2, current_date] = float(''.join([i for i in second if i.isdigit()])) ##записываем цифры в таблицу

##кристальная, 2шт
second = first.find("div", id = "6c0e3e2de3654cc09e3e185149df24be").text.split('х')[1]
df.loc[3, current_date] = float(''.join([i for i in second if i.isdigit()])) ##аналогично
##сохраняем таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
