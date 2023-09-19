import csv
import matplotlib.pyplot as plt

from datetime import datetime

filename = 'data/AQW00061705.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    #print(header_row)

    #for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # get dates, high temperatures from this file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[1], '%Y-%m')
        dates.append(current_date)
        #print(type(high))
        highs.append(eval(row[88]))
        lows.append(eval(row[90]))

# plot the high temperatures
plt.style.use('classic')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# format plot
plt.title("Daily high and low temperatures, January 2023", fontsize=24)
plt.xlabel('', fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()

#print(highs)