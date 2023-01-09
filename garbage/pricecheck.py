from datetime import date ##дата и время
import pandas as pd ##работа с csv

current_date = str(date.today())
df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')

print("Для анализа доступны даты с " + list(df.columns)[2] + " по " + list(df.columns)[-1])

date1 = str(input("Введите первую дату в формате ГГГГ-ММ-ДД: "))
flag = True
while flag == True:
    try:
        df.loc[0, date1]
        flag = False
    except Exception:
        date1 = str(input("Дата введена неверно, попробуйте еще раз: "))

    
date2 = str(input("Введите вторую дату в формате ГГГГ-ММ-ДД: "))
flag = True
while flag == True:
    try:
        df.loc[0, date2]
        flag = False
    except Exception:
        date2 = str(input("Дата введена неверно, попробуйте еще раз: "))

day1 = int(date1.split("-")[2])
day2 = int(date2.split("-")[2])
month1 = int(date1.split("-")[1])
month2 = int(date2.split("-")[1])
year1 = int(date1.split("-")[0])
year2 = int(date2.split("-")[0])

if year1 != year2:
    if year1 > year2:
        datenew = date1
        dateold = date2
    else:
        datenew = date2
        dateold = date1
else:
    if month1 != month2:
        if month1 > month2:
            datenew = date1
            dateold = date2
        else:
            datenew = date2
            dateold = date1
    else:
        if day1 != day2:
            if day1 > day2:
                datenew = date1
                dateold = date2
            else:
                datenew = date2
                dateold = date1
        else:
            print("Даты одинаковые")
            datenew = date1
            dateold = date2

tip = int(input("Выберите тип вывода: 1 - полный, 2 - короткий ---> "))
if tip == "1":
    for i in range(0,19):
        change = str(round(((df.loc[i, datenew] - df.loc[i, dateold])/df.loc[i, dateold])*100, 2))
        name = str(df.loc[i, "Название"])
        kolvo = str(df.loc[i, "Кол-во"])
        oldprice = str(df.loc[i, dateold])
        newprice = str(df.loc[i, datenew])
        rezult_message = "Вода " + name + "("+ kolvo + ") на " + dateold +" стоила " + oldprice + " руб, на " + datenew + " стоит " + newprice + " руб, изменение составило: " + change + "%"
        print(rezult_message)
elif tip == "2":
    for i in range(0,19):
        change = str(round(((df.loc[i, datenew] - df.loc[i, dateold])/df.loc[i, dateold])*100, 2))
        name = str(df.loc[i, "Название"])
        kolvo = str(df.loc[i, "Кол-во"])
        rezult_message = name + "("+kolvo+"): изменение " + change + "%"
        print(rezult_message)
else:
    print("Ошибка") 
      
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
