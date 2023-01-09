from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv
current_date = str(date.today())
df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

url_artenza = "https://arkhiz74.ru/page/19litrov/"
pages = requests.get(url_artenza).text  ##делаем запрос на сайт, получаем html

soup = bs(pages, "lxml")        ##конвертируем полученный html в удобный формат

first = soup.find("div", class_ = "content") ##ищем на сайте необходимый элемент
tara = first.find_all("span", style = 'font-size: large;')[6].text.split("тары")[1]

df.loc[4, current_date] = float(''.join([i for i in tara if i.isdigit()]))
df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
