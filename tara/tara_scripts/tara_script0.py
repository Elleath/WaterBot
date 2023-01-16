from bs4 import BeautifulSoup as bs ## парсер html 
from datetime import date ##дата и время
import pandas as pd ##работа с csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time
current_date = str(date.today())
options = Options()
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir=C:/Users/Kirill/Desktop/profiles')
options.add_argument('--profile-directory=Profile 1') 
#options.add_argument("--headless") 
df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')

browser = webdriver.Chrome(options=options)
browser.set_window_size(1051, 806)
browser.get("https://живаякапля.рф/catalog/water/water_drinking_zhivaya_kaplya_19l/?oid=1025")
time.sleep(2)


button1 = browser.find_element("xpath", '//*[@id="bx_117848907_1012_prop_842_list"]/li[2]/span/span')
button1.click()
time.sleep(2)
without_tara = float(browser.find_element("xpath", '//*[@id="content"]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/span[1]').text)
button2 = browser.find_element("xpath", '//*[@id="bx_117848907_1012_prop_842_list"]/li[1]/span/span')
button2.click()
time.sleep(2)
with_tara = float(browser.find_element("xpath", '//*[@id="content"]/div[2]/div/div/div/div/div/div/div/div[2]/div/div[2]/div[1]/div[1]/div[1]/span[1]').text)
df.loc[0, current_date] = with_tara - without_tara  ##и записываем его в таблицу
df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
