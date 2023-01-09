from bs4 import BeautifulSoup as bs ## парсер html 
import requests ## запросы на сайты
from datetime import date ##дата и время
import pandas as pd ##работа с csv
current_date = str(date.today())
df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
  }

url_lubimaya = "https://vodalubima.ru"

pages = requests.get(url_lubimaya, headers=headers).text

soup = bs(pages, "lxml")        ##конвертируем полученный html в удобный формат

first = soup.find("div", id = "rec42533675") ##ищем на сайте необходимый элемент
tara = first.find_all("div", class_ = 't776__price-value js-product-price notranslate')[2].text
df.loc[5, current_date] = float(''.join([i for i in tara if i.isdigit()]))
df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
