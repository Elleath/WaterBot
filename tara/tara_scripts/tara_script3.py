from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv
current_date = str(date.today())
df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

url_lider = "https://artvod.ru/catalog/lider19-2/"
pages = requests.get(url_lider).text  ##делаем запрос на сайт, получаем html

soup = bs(pages, "lxml")        ##конвертируем полученный html в удобный формат

first = soup.find("div", class_ = "product-data-item") ##ищем на сайте необходимый элемент
tara = first.find("div", class_ = "name793").text.strip()

df.loc[3, current_date] = float(''.join([i for i in tara if i.isdigit()]))
df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
