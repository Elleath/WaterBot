import runpy ##запуск скриптов
from datetime import date ##дата и время
import time ##для sleep
import pandas as pd ##работа с csv

current_date = str(date.today()) ##определяем текущую дату
errors = []                      ##список ошибок для повторного перезапуска

df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
##открываем таблицу
try:
    df.loc[0, current_date]               ##проверяем есть ли в ней текущая дата, если есть
    print("Сегодня данные уже собирались")##то данные не собираем (уже собирались)
except Exception:
    df.loc[:, current_date]= float(-1)   ##если даты нет, то добавляем
    df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
    ##сохраняем таблицу
    i = 0
    while i <= 14:
        name = "C:/Users/Kirill/Desktop/project/scripts/script" + str(i) + ".py"
        try:
            runpy.run_path(name)      ##пробуем запустить поочередно скрипты
            i = i + 1
        except Exception:
            print("Ошибка в скрипте №" + str(i)) ##если скрипт не сработал, то пишем
            errors.append(i)                    ##и добавляем в список ошибок
            i = i + 1

print("Ошибки: ", errors)

if errors != []:    ##повторно перезапускаем несработавшие скрипты
    for j in errors:
        name = "C:/Users/Kirill/Desktop/project/scripts/script" + str(j) + ".py"
        try:
            runpy.run_path(name)
        except Exception:
            print("Ошибка в скрипте №" + str(j) + ", попытка 2" )
      
time.sleep(10)

