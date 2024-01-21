# This is a sample Python script.

# Press Skift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
from datetime import datetime, timezone, time

import pause as pause
from requests import get, exceptions

import matplotlib.pyplot as plt
import numpy as np
import winsound
from matplotlib import animation

r = get('http://192.168.0.157/api/v1/data')
packages_json = r.json()
print(packages_json)
totalFörbrukning = packages_json['total_power_import_t1_kwh']
package_power = packages_json['active_power_w']

#packages_str = json.dumps(packages_json, indent=2)

print('T1 kWh: ',totalFörbrukning)

print('Active Power: ',package_power)

print('')
#print(packages_str)

aktualTime = datetime.now()
#tid = datetime.strptime(str(aktualTime), "%H")
print("Hour: " + str(aktualTime.hour))
print("Current time: " + str(aktualTime))
timme = aktualTime.hour
timconsumptiom = 0
startFörbrukningHelTimme = totalFörbrukning

#x = np.array(["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"])

xdata = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

#y = np.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])
ydata = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
bars = plt.bar(xdata, ydata, facecolor='green', alpha=0.75)
plt.ylim(0,3)
#plt.bar_label("5")


''''fig, ax = plt.subplots()
#p = ax.bar("apa", 5, 0.6, label='test', bottom=0)
p = ax.bar(xdata,ydata, 0.6, label='test', bottom=0)
#ax.bar_label(p, label_type='center')
#ydata[2] = 3
p = ax.bar(0, 3, 0.6, label='test', bottom=0)
ax.bar_label(p, label_type='center')
p = ax.bar(0, 2, 0.6, label='test', bottom=3)
plt.ylim(0,6)
ax.bar_label(p, label_type='edge')
#x = np.array([1, 2, 3, 4])
#y = np.array([3, 8, 1, 10])'''''


#plt.bar(xdata, ydata)
plt.ion()
plt.pause(1)


#plt.draw()
#plt.plot()

#plt.show()

#plt.show(block=False)

while (True):
    try:
        r = get('http://192.168.0.157/api/v1/data')
        packages_json = r.json()


        package_t1 = packages_json['total_power_import_t1_kwh']
        package_power = packages_json['active_power_w']
        wifi_styrka = packages_json['wifi_strength']
        timconsumptiom = package_t1 - startFörbrukningHelTimme

        ydata[timme] = timconsumptiom
        # Set different coulour of bar depending on the consumed energi
        if timconsumptiom < 0.01:
            #bar(xdata, ydata, facecolor='green', alpha=0.75)
            bars[timme].set_height(timconsumptiom)
            bars[timme].set_facecolor('green')

            bars[timme].set_label(timconsumptiom)
        else:
            #plt.bar(xdata, ydata, facecolor='red', alpha=0.75)
            bars[timme].set_height(timconsumptiom)
            bars[timme].set_facecolor('red')
            bars[timme].set_label(timconsumptiom)

        bars[24].set_height(package_power/1000)
        if package_power < 1000:
            bars[24].set_facecolor('green')
        else:
            bars[24].set_facecolor('red')
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 100  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
            winsound.Beep(frequency, duration)

        #Test av minne för högsta effekt
        ''''       p = ax.bar(24, 3, 0.6, label='edge', bottom=0)
        ax.bar_label(p, label_type='center', color='red')
        p = ax.bar(24, 2, 0.6, label='test', bottom=3)
        plt.ylim(0, 6)
        ax.bar_label(p, label_type='edge', color='green')'''''


        #package_power
        plt.pause(1)

        print('Wifi: ', wifi_styrka, 'Total power: ', package_t1, "Aktuell effekt: ", package_power, "Timförbrukning: ",  timconsumptiom)
        #print('Active Power: ', package_power)

        #y[timme] = timconsumptiom
        if (datetime.now().hour != timme):
            print("Ny timme!")
            timconsumptiom = 0
            startFörbrukningHelTimme = packages_json['total_power_import_t1_kwh']
            timme = datetime.now().hour
        #pause.seconds(1)
        #plt.pause(1)

    except exceptions.HTTPError as errh:
        print("HTTP Error")
        print(errh.args[0])
    except exceptions.ReadTimeout as errrt:
        print("Time out")
    except exceptions.ConnectionError as conerr:
        print("Connection error")

'''

# Detta funkar
plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

data = [1, 4, 3, 2, 3, 5, 7]
colors = ['red', 'yellow', 'blue', 'green', 'black']
bars = plt.bar(data, data, facecolor='green', alpha=1)
plt.show()

def animate(frame):
   global bars
   index = np.random.randint(1, 7)
   bars[frame].set_height(index)
   bars[frame].set_facecolor(colors[np.random.randint(0, len(colors))])

ani = animation.FuncAnimation(fig, animate, frames=7)

plt.show()'''

'''
plt.rcParams["figure.figsize"] = [8.50, 3.50]
plt.rcParams["figure.autolayout"] = True

fig = plt.figure()

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
colors = ['red', 'yellow', 'blue', 'green', 'black']
bars = plt.bar(data, 30, facecolor='green', alpha=0.75)

def animate(frame):
   global bars
   index = np.random.randint(1, 24)
   bars[frame].set_height(index)
   bars[frame].set_facecolor(colors[np.random.randint(0, len(colors))])

ani = animation.FuncAnimation(fig, animate, frames=5)

plt.show()'''
