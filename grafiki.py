import sys
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas)
from matplotlib.figure import Figure
import pandas as pd

with open("temp.txt", "r") as f:
    nomer = int(f.read())

df = pd.read_csv("C:/Users/Kirill/Desktop/project/output.csv", delimiter = ",", encoding='utf-8')
x_labels = []
x = []
y = []
dates = []
watername = df.loc[nomer, "Название"]
for i in range(2, len(list(df.columns))):
    if df.columns[i].split("-")[2] == "25":
        nazv = df.columns[i].split("-")[1]
        x_labels.append(nazv)
        dates.append(df.columns[i])
    else:
        pass
    
for data in dates:
    if df.loc[nomer, data] == -1.0:
        to_remove = data.split("-")[1]
        x_labels.remove(to_remove)
    else:
        price = df.loc[nomer, data]
        y.append(price)
i = 1
while len(x) != len(x_labels):
    x.append(i)
    i += 1
df.to_csv( "C:/Users/Kirill/Desktop/project/output.csv" , index = False, encoding='utf-8')

fig=Figure()
canvas=FigureCanvas(fig)
ax=canvas.figure.add_subplot(111)
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.set_title('Вода "' + watername + '"')
ax.set_xlabel('Месяцы')
ax.set_ylabel('Цена на 25 число (руб)')
ax.plot(x,y)
fig.savefig("grafik.png", dpi = 150)

#app=QtWidgets.QApplication(sys.argv)
#app.exec()



