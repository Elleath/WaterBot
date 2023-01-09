from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv
current_date = str(date.today())
df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

url_oazis = "https://www.74mv.ru/katalog/gornyj-oazis"
pages = requests.get(url_oazis).text  ##делаем запрос на сайт, получаем html

soup = bs(pages, "lxml")        ##конвертируем полученный html в удобный формат

first = soup.find("div", class_ = "row") ##ищем на сайте необходимый элемент
tara = first.find("p", class_ = "product_s_desc").text.split("тары")

df.loc[2, current_date] = float(''.join([i for i in tara[2] if i.isdigit()]))
df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
