import runpy ##запуск скриптов
from datetime import date ##дата и время
import time
import pandas as pd ##работа с csv

current_date = str(date.today())
logs_errors = []

df = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')


try:
    df.loc[0, current_date]
    print("Сегодня данные уже собирались")
except Exception:
    df.loc[:, current_date]= float(-1)
    df.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
    i = 0
    while i <= 9:
        name = "C:/Users/Kirill/Desktop/project/tara/tara_scripts/tara_script" + str(i) + ".py"
        try:
            runpy.run_path(name)
            i = i + 1
        except Exception:
            print("Ошибка в скрипте №" + str(i))
            logs_errors.append(i)
            i = i + 1
            
if logs_errors == []:
    with open("C:/Users/Kirill/Desktop/project/logs/logs_tara.txt", "a") as logs:
        logs.write(current_date + "\n")
        logs.write("Ошибок нет")
else:
    with open("C:/Users/Kirill/Desktop/project/logs/logs_tara.txt", "a") as logs:
        logs.write(current_date + "\n")
        for log in logs_errors:
            logs.write("Ошибка в скрипте " + str(log) + "\n")

time.sleep(10)


