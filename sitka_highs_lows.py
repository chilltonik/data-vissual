import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #Вывод заголовка таблицы
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    #Чтение дат, максимальных и минимальных температур
    dates, highs, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        highs.append(int(row[5]))
        lows.append(int(row[6]))

#Нанесение данных на диаграму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

#Форматирование диаграммы
plt.title("Daily high and low temperatures - 2018", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#plt.axis([0, len(highs), min(highs), max(highs)])

plt.show()
fig.savefig('images/second.png')