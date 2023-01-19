import pandas as pd ##работа с таблицами
import telebot ##сам бот
from datetime import date, timedelta ##дата и время
import time ##для sleep
from telebot import types 
import runpy ##для запуска скриптов

bot = telebot.TeleBot('5639471781:AAFjwXx-Mvb3rH2HBpJMVgGR12Bs20fN88A')

date1 = ""
date2 = ""
#current_date_old = ""

@bot.message_handler(content_types=['text', 'document', 'photo'])

def hello(message):
    global current_date_old
    if message.text == "/start":
        bot.send_message(message.from_user.id, "Приветствуем Вас в нашем телеграмм-боте")
        time.sleep(1)
        bot.send_message(message.from_user.id, "Здесь вы можете сравнить цены воды на две любые даты и построить график изменения цены")
        time.sleep(1)
        
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        btn1 = types.KeyboardButton(text='Сравнить цены')
        btn2 = types.KeyboardButton(text='Построить графики изменения цены')
        btn3 = types.KeyboardButton(text='Цены на тару')
        btn4 = types.KeyboardButton(text='Получить полную таблицу с ценами')
        keyboard.add(btn1,btn2,btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите желаемое:', reply_markup=keyboard)
        bot.register_next_step_handler(message, choice)
      
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        btn1 = types.KeyboardButton(text='Сравнить цены')
        btn2 = types.KeyboardButton(text='Построить графики изменения цены')
        btn3 = types.KeyboardButton(text='Цены на тару')
        btn4 = types.KeyboardButton(text='Получить полную таблицу с ценами')
        keyboard.add(btn1,btn2,btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите желаемое:', reply_markup=keyboard)
        bot.register_next_step_handler(message, choice)
        
def choice(message):
    choice1 = message.text ##принимаем введенное пользователем значение, преобразуем в текст
    if choice1 == "Сравнить цены": ##сравниваем значение
        analysis(message)   ##переходим в соответствующую функцию
    elif choice1 == "Построить графики изменения цены":
        spisok =    """Выберите марку воды (все от 2 шт): \n
                1 - Живая капля \n
                3 - Кристальная \n
                4 - Горный оазис \n
                6 - Лидер \n
                8 - Лидер Платинум \n
                10 - Лидер Профи \n
                12 - Артенза \n
                13 - Любимая \n
                15 - Чебаркульский исток \n
                17 - Ниагара Премиум \n
                19 - Ниагара \n
                21 - Власов ключ \n
                23 - Люкс \n
                    """
        
        bot.send_message(message.from_user.id, spisok, reply_markup=types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, grafik) ##получаем значение и переходим в функцию
    elif choice1 == "Цены на тару":
        tara(message)    ##переходим в соответствующую функцию
    elif choice1 == "Получить полную таблицу с ценами":
        full_table(message)
    else:
        bot.send_message(message.from_user.id, "Ошибка")
        hello(message)  ##откатываемся назад при неверном вводе
    

def analysis(message):
    global date1, date2
    if date1 == "" or date2 == "":
        df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
        datesmessage = "Для анализа доступны даты с " + list(df.columns)[2] + " по " + list(df.columns)[-1]
        bot.send_message(message.from_user.id, datesmessage, reply_markup=types.ReplyKeyboardRemove())
        time.sleep(1)
        #df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')  
        bot.send_message(message.from_user.id, "Введите первую дату в формате ГГГГ-ММ-ДД")
        bot.register_next_step_handler(message, get_date1)
    else:
        #bot.send_message(message.from_user.id, "Использовать уже введенные даты? 1 - да, 2 - нет")
        keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        btn1 = types.KeyboardButton(text='Да')
        btn2 = types.KeyboardButton(text='Нет')
        keyboard1.add(btn1,btn2)
        bot.send_message(message.chat.id, 'Использовать уже введеные даты?', reply_markup=keyboard1)
        
        bot.register_next_step_handler(message, use_old_dates)

def use_old_dates(message):
    global date1,date2
    if message.text == "Нет":
        date1 = ""
        date2 = ""
        analysis(message)
    elif message.text == "Да":
         bot.send_message(message.from_user.id, "Получены даты: " + date1 + " и " + date2, reply_markup=types.ReplyKeyboardRemove())
         #bot.send_message(message.from_user.id, "Выберите тип вывода: 1 - полный, 2 - короткий, 3 - txt, 4 - csv")
         keyboard2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
         btn1 = types.KeyboardButton(text='Полный (в чат)')
         btn2 = types.KeyboardButton(text='Короткий (в чат)')
         btn3 = types.KeyboardButton(text='Полный в txt')
         btn4 = types.KeyboardButton(text='Полный в xlsx')
         keyboard2.add(btn1,btn2,btn3,btn4)
         bot.send_message(message.chat.id, 'Выберите тип вывода: ', reply_markup=keyboard2)
         bot.register_next_step_handler(message, tip)
    else:
        bot.send_message(message.from_user.id, "Ошибка")
        analysis(message)
    

current_date = str(date.today())

def returning(message):
    if message.text == "обратно" or message.text == "назад" or message.text == "Обратно" or message.text == "Назад":
        #if str(date.today()) == current_date_old:
            #pass
        #else:
            #try:
                #fast_check(message)
            #except Exception:
                #pass
        keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
        btn1 = types.KeyboardButton(text='Сравнить цены')
        btn2 = types.KeyboardButton(text='Построить графики изменения цены')
        btn3 = types.KeyboardButton(text='Цены на тару')
        btn4 = types.KeyboardButton(text='Получить полную таблицу с ценами')
        keyboard.add(btn1,btn2,btn3, btn4)
        bot.send_message(message.chat.id, 'Выберите желаемое:', reply_markup=keyboard)
        bot.register_next_step_handler(message, choice)
    else:
        return 0
        

def get_date1(message):
    global date1;
    if returning(message) == 0:
        date1 = message.text
        df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
        try:
            df.loc[0, date1]
            bot.send_message(message.from_user.id, "Верно")
            bot.send_message(message.from_user.id, "Введите вторую дату в формате ГГГГ-ММ-ДД")
            bot.register_next_step_handler(message, get_date2)
            
        except Exception:
            bot.send_message(message.from_user.id, "Дата введена неверно, попробуйте еще раз")
            bot.register_next_step_handler(message, get_date1)
        #df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')

def get_date2(message):
    global date2;
    if returning(message) == 0:
        date2 = message.text
        df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
        try:
            df.loc[0, date2]
            if date1 == date2:
                bot.send_message(message.from_user.id, "Вы ввели одинаковые даты, выберите другую")
                bot.register_next_step_handler(message, get_date2)
            else:
                bot.send_message(message.from_user.id, "Верно")
                bot.send_message(message.from_user.id, "Получены даты: " + date1 + " и " + date2)
                #bot.send_message(message.from_user.id, "Выберите тип вывода: 1 - полный, 2 - короткий, 3 - txt, 4 - csv")
                keyboard2 = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=False, one_time_keyboard=True)
                btn1 = types.KeyboardButton(text='Полный (в чат)')
                btn2 = types.KeyboardButton(text='Короткий (в чат)')
                btn3 = types.KeyboardButton(text='Полный в txt')
                btn4 = types.KeyboardButton(text='Полный в xlsx')
                keyboard2.add(btn1,btn2,btn3,btn4)
                bot.send_message(message.chat.id, 'Выберите тип вывода: ', reply_markup=keyboard2)
                bot.register_next_step_handler(message, tip)
                #df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')
        except Exception:
            bot.send_message(message.from_user.id, "Дата введена неверно, попробуйте еще раз")
            bot.register_next_step_handler(message, get_date2)

def tip(message):
    if returning(message) == 0:
        tip = message.text
        df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
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
                    datenew = date1
                    dateold = date2
        if tip == "Полный (в чат)":
            for i in range(0,24):
                name = str(df.loc[i, "Название"])
                kolvo = str(df.loc[i, "Кол-во"])
                oldprice = df.loc[i, dateold]
                newprice = df.loc[i, datenew]

                if oldprice != -1.0 and newprice != -1.0:
                    change = round(((df.loc[i, datenew] - df.loc[i, dateold])/df.loc[i, dateold])*100, 2)
                    if change >= 0:
                        rezult_message = "Вода " + name + "("+ kolvo + ") на " + dateold +" стоила " + str(oldprice) + " руб, на " + datenew + " стоит " + str(newprice) + " руб, изменение составило: +" + str(change) + "%"
                        bot.send_message(message.from_user.id, rezult_message, reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(1)
                    else:
                        rezult_message = "Вода " + name + "("+ kolvo + ") на " + dateold +" стоила " + str(oldprice) + " руб, на " + datenew + " стоит " + str(newprice) + " руб, изменение составило: " + str(change) + "%"
                        bot.send_message(message.from_user.id, rezult_message, reply_markup=types.ReplyKeyboardRemove())
                        time.sleep(1)
                else:
                    rezult_message = "Вода " + name + "("+ kolvo + ") на " + dateold +" стоила " + str(oldprice) + " руб, на " + datenew + " стоит " + str(newprice) + " руб, не могу посчитать изменение"
                    bot.send_message(message.from_user.id, rezult_message, reply_markup=types.ReplyKeyboardRemove())
                    time.sleep(1)
        elif tip == "Короткий (в чат)":
            short_message = "" ##создаем сообщение, которое выведет бот
            for i in range(0,24): ##перебираем все строки из таблицы
                name = str(df.loc[i, "Название"])
                kolvo = str(df.loc[i, "Кол-во"])
                oldprice = df.loc[i, dateold]     ##берем элементы из таблицы
                newprice = df.loc[i, datenew]
                if oldprice != -1.0 and newprice != -1.0: ##проверяем, что цена была собрана
                    ##считаем изменение цены
                    change = round(((df.loc[i, datenew] - df.loc[i, dateold])/df.loc[i, dateold])*100, 2)
                    if change == 0: ##если изменений нет, то пропускаем
                        pass
                    elif change > 0: ##если больше 0, то добавляем в итоговое сообщение строку с "+"
                        short_message += name + "("+kolvo+"): изменение +" + str(change) + "% \n"
                        
                    else: ##если меньше 0, то добавляем строку без знака (минус появится сам)
                        short_message += name + "("+kolvo+"): изменение " + str(change) + "%\n"
                        
                else: ##если данные не были собраны (цена = -1.0), то добавляем строку
                    short_message += name + "("+kolvo+"): нет информации \n"
                    
            if short_message == "": ##если итоговое сообщение пустое, то пишем, что изменений нет
                bot.send_message(message.from_user.id, "Изменений нет", reply_markup=types.ReplyKeyboardRemove())
            else: ##иначе отправляем итоговое сообщение
                bot.send_message(message.from_user.id, short_message, reply_markup=types.ReplyKeyboardRemove())
        elif tip == "Полный в txt":
            with open("C:/Users/Kirill/Desktop/project/rezult.txt", "w") as f:
                for i in range(0,24):
                    name = str(df.loc[i, "Название"])
                    kolvo = str(df.loc[i, "Кол-во"])
                    oldprice = df.loc[i, dateold]
                    newprice = df.loc[i, datenew]

                    if oldprice != -1.0 and newprice != -1.0:
                        change = round(((df.loc[i, datenew] - df.loc[i, dateold])/df.loc[i, dateold])*100, 2)
                        if change >= 0:
                            rezult_message = "Вода " + name + "("+ kolvo + ") на " + dateold +" стоила " + str(oldprice) + " руб, на " + datenew + " стоит " + str(newprice) + " руб, изменение составило: +" + str(change) + "%"
                            f.write(rezult_message + '\n')
                            #time.sleep(1)
                        else:
                            rezult_message = "Вода " + name + "("+ kolvo + ") на " + dateold +" стоила " + str(oldprice) + " руб, на " + datenew + " стоит " + str(newprice) + " руб, изменение составило: " + str(change) + "%"
                            f.write(rezult_message + '\n')
                            #time.sleep(1)
                    else:
                        rezult_message = "Вода " + name + "("+ kolvo + ") на " + dateold +" стоила " + str(oldprice) + " руб, на " + datenew + " стоит " + str(newprice) + " руб, не могу посчитать изменение"
                        f.write(rezult_message + '\n')
                        #time.sleep(1)
            doc = open("C:/Users/Kirill/Desktop/project/rezult.txt", 'r')
            bot.send_document(message.from_user.id, doc)
            doc.close()

        elif tip == "Полный в xlsx":
            #df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
            with open("C:/Users/Kirill/Desktop/project/forCSV/rezult1.txt", "w", encoding = "utf-8") as f:
                f.write("Название,Кол-во," + dateold + "," + datenew + ",Изменение\n") ##открываем txt для записи
                for i in range(0,24): ##перебираем строки
                    name = str(df.loc[i, "Название"])
                    kolvo = str(df.loc[i, "Кол-во"]) ##берем необходимые данные из таблицы
                    oldprice = df.loc[i, dateold]
                    newprice = df.loc[i, datenew]

                    if oldprice != -1.0 and newprice != -1.0:
                        change = round(((df.loc[i, datenew] - df.loc[i, dateold])/df.loc[i, dateold])*100, 2)
                        if change >= 0:
                            rezult_message = name + "," + kolvo + "," + str(oldprice) + "," + str(newprice) + "," + "+" + str(change) + "%"
                            f.write(rezult_message + '\n')  ##записываем данные в файл в форме csv(разеделение через запятую)
                            #time.sleep(1)
                        else:
                            rezult_message = name + "," + kolvo + "," + str(oldprice) + "," + str(newprice) + "," + str(change) + "%"
                            f.write(rezult_message + '\n')
                            #time.sleep(1)
                    else:
                        rezult_message = name + "," + kolvo + "," + str(oldprice) + "," + str(newprice) + "," + "-1.0"
                        f.write(rezult_message + '\n')
                        #time.sleep(1)
            #df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')

            df1 = pd.read_csv('C:/Users/Kirill/Desktop/project/forCSV/rezult1.txt',delimiter = ",", encoding='utf-8')
            df1.to_excel('C:/Users/Kirill/Desktop/project/forCSV/rezult_change.xlsx', index = False)
            ##реобразуем полученный txt в xlsx
            doc = open("C:/Users/Kirill/Desktop/project/forCSV/rezult_change.xlsx", 'rb')
            bot.send_document(message.from_user.id, doc) ##отправляем пользователю
            doc.close()    
        else:
            bot.send_message(message.from_user.id, "Ошибка")
            #bot.register_next_step_handler(message, tip)
        #df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')

        keyboard = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton(text='Заново')
        keyboard.add(btn1)
        bot.send_message(message.chat.id, 'Если хотите начать заново, то нажмите кнопку', reply_markup=keyboard)
        #bot.register_next_step_handler(message, perezapusk)

def grafik(message):
    if returning(message) == 0:
        try:
            nomer = int(message.text)  ##выбранную пользователем воду (номер) переводим в цифру     
            if nomer in [1,3,4,6,8,10,12,13,15,17,19,21,23]: ##проверяем, что она есть в списке
                with open("temp.txt", "w") as f:
                    f.write(str(nomer)) ##записываем номер в временный файл
                runpy.run_path("C:/Users/Kirill/Desktop/project/grafiki.py") ##запускаем внешний скрипт
                time.sleep(3) ##задержка для корректной работы внешного скрипта
                sendmessage = open("C:/Users/Kirill/Desktop/project/grafik.png", "rb") 
                bot.send_photo(message.chat.id, sendmessage) ##отправляем построенный график в чат
                sendmessage.close()
                time.sleep(1)
                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
                btn1 = types.KeyboardButton(text='Заново')
                keyboard.add(btn1) ##предлагаем начать заново и добавляем кнопку "заново"
                bot.send_message(message.chat.id, 'Если хотите начать заново, то нажмите кнопку', reply_markup=keyboard)
            else: ##если номера нет в списке, то идем назад
                bot.send_message(message.from_user.id, "Неверный ввод, возврат")
                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
                btn1 = types.KeyboardButton(text='Сравнить цены')
                btn2 = types.KeyboardButton(text='Построить графики изменения цены')
                btn3 = types.KeyboardButton(text='Цены на тару')
                btn4 = types.KeyboardButton(text='Получить полную таблицу с ценами')
                keyboard.add(btn1,btn2,btn3, btn4)
                bot.send_message(message.chat.id, 'Выберите желаемое:', reply_markup=keyboard)
                bot.register_next_step_handler(message, choice)
        except Exception: ##если ввод неверный, идем назад
                bot.send_message(message.from_user.id, "Неверный ввод, возврат")
                keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=False, one_time_keyboard=True)
                btn1 = types.KeyboardButton(text='Сравнить цены')
                btn2 = types.KeyboardButton(text='Построить графики изменения цены')
                btn3 = types.KeyboardButton(text='Цены на тару')
                btn4 = types.KeyboardButton(text='Получить полную таблицу с ценами')
                keyboard.add(btn1,btn2,btn3, btn4)
                bot.send_message(message.chat.id, 'Выберите желаемое:', reply_markup=keyboard)
                bot.register_next_step_handler(message, choice)

def fast_check(message):
    global current_date_old
    fast_message = "Сегодня изменились цены: \n"
    df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
    for i in range(0,24):
        name = str(df.loc[i, "Название"])
        kolvo = str(df.loc[i, "Кол-во"])
        oldprice = df.loc[i, str(date.today() - timedelta(days=1))]
        newprice = df.loc[i, str(date.today())]

        if oldprice != -1.0 and newprice != -1.0:
            change = round(((df.loc[i, str(date.today())] - df.loc[i, str(date.today() - timedelta(days=1))])/df.loc[i, str(date.today() - timedelta(days=1))])*100, 2)
            if change != 0:
                if change >= 0:
                    fast_message = fast_message + name + "("+kolvo+"): +" + str(change) + "% \n"
                else:
                    fast_message = fast_message + name + "("+kolvo+"): " + str(change) + "% \n"
            else:
                pass
        else:
            fast_message = fast_message + name + "("+kolvo+"): данные не получены \n"
    
    df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')

    if fast_message == "Сегодня изменились цены: \n":
        bot.send_message(message.from_user.id, "Сегодня изменений цены нет")
        current_date_old = str(date.today())
    else:
        bot.send_message(message.from_user.id, fast_message)
        current_date_old = str(date.today())
        time.sleep(1)

def tara(message):
    df_tara = pd.read_csv("C:/Users/Kirill/Desktop/project/tara/tara_output.csv", delimiter = ",", encoding='utf-8')
    last_date = str(list(df_tara.columns)[-1])
    tara_message = "Актуально на " + last_date + ": \n"
    for i in range(0,10):
        name_tara = str(df_tara.loc[i, "Название"])
        if df_tara.loc[i, last_date] == -1.0:
            pass
        else:
            tara_message = tara_message + name_tara + ": " + str(df_tara.loc[i, last_date]) + " рублей \n"
    #df_tara.to_csv( "C:/Users/Kirill/Desktop/project/tara/tara_output.csv" , index = False, encoding='utf-8')
    bot.send_message(message.from_user.id, tara_message, reply_markup=types.ReplyKeyboardRemove())
    time.sleep(1)
    #bot.send_message(message.from_user.id, "Если хотите начать заново, то отправьте любое сообщение")
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='Заново')
    keyboard.add(btn1)
    bot.send_message(message.chat.id, 'Если хотите начать заново, то нажмите кнопку', reply_markup=keyboard)

def full_table(message):
    df_table = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
    df_table.to_excel("C:/Users/Kirill/Desktop/project/full_result.xlsx", index = False)

    full_table = open("C:/Users/Kirill/Desktop/project/full_result.xlsx", 'rb')
    bot.send_document(message.from_user.id, full_table)
    full_table.close()
    keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton(text='Заново')
    keyboard.add(btn1)
    bot.send_message(message.chat.id, 'Если хотите начать заново, то нажмите кнопку', reply_markup=keyboard)
          
#def perezapusk(message):
   # analysis(message)
    
bot.polling(none_stop=True, interval=0)
