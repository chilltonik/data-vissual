import csv
from datetime import datetime
from matplotlib import pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    dates, highs, lows = [], [], []
    for row in reader:
        dates.append(datetime.strptime(row[2], '%Y-%m-%d'))
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {datetime.strptime(row[2], '%Y-%m-%d')}")
            highs.append(0)
            lows.append(0)
        else:
            highs.append(high)
            lows.append(low)

#Нанесение данных на диаграму
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

ax.plot(dates, highs, c='red')
ax.plot(dates, lows, c='blue')

#Форматирование диаграммы
plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=20)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel('Temperature (F)', fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)
#plt.axis([0, len(highs), min(highs), max(highs)])

plt.show()
fig.savefig('images/first.png')