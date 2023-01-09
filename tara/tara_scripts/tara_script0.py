from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv
current_date = str(date.today())
df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

##живая капля, 1 шт
url_jivaya_voda1 = "https://живаякапля.рф/catalog/voda/voda_pitevaya_zhivaya_kaplya_19l/?oid=1135"
pages = requests.get(url_jivaya_voda1).text  ##делаем запрос на сайт, получаем html

soup = bs(pages, "lxml")        ##конвертируем полученный html в удобный формат

first = soup.find("div", class_ = "wraps hover_shine") ##ищем на сайте необходимый элемент
with_tara = float(first.find("span", class_ = "price_value").text)


url_jivaya_voda2 = "https://живаякапля.рф/catalog/voda/voda_pitevaya_zhivaya_kaplya_19l/?oid=1136"
pages = requests.get(url_jivaya_voda2).text  ##делаем запрос на сайт, получаем html
soup = bs(pages, "lxml")       

first = soup.find("div", class_ = "wraps hover_shine") 
without_tara = float(first.find("span", class_ = "price_value").text)

df.loc[0, current_date] = with_tara - without_tara  ##и записываем его в таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
