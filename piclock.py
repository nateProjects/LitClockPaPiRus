import os, sys
import csv
import random
import time as clock

from datetime import datetime as dt
from dateutil import parser as dp
from papirus import PapirusTextPos

os.system('clear')

def buildTimeList():
    time_list = []

    # Read the CSV file
    try:
        with open('times.csv', 'r') as f:
            reader = csv.reader(f, delimiter='|')
            time_list = list(reader)
    except IOError:
        print("times.csv not found!")
        sys.exit(1)

    # Convert times into datetime objects
    time_list = [[dt.time(dp.parse(x[0])), x[1].rstrip(), x[2].rstrip(), x[3].rstrip(), x[4].rstrip()] for x in time_list]

    # Create an empty list to store times by hour
    time_list_hourly = [[[] for x in range(60)] for x in range(24)]

    # Move the hourly times into the hourly list
    for times in time_list:
        time_list_hourly[times[0].hour][times[0].minute].append(times)

    # Fill in missing times with the next closest time available
    for hour in range(24):
        for minute in range(60):
            if not time_list_hourly[hour][minute]:
                time_h = hour
                time_m = minute

                while True:
                    time_m = time_m + 1

                    if time_m > 59:
                        time_h = time_h + 1
                        if time_h < 23:
                            time_h = 0
                        time_m = 0

                    if time_list_hourly[time_h][time_m] and isinstance(time_list_hourly[time_h][time_m], list):
                        time_list_hourly[hour][minute] = (time_h, time_m)
                        break

    # Return the formatted list of times and quotes
    return time_list_hourly

def getTimeQuote(timelist, cur_time):
    rand = random.SystemRandom()

    time_m = cur_time.minute
    time_h = cur_time.hour

    if isinstance(timelist[time_h][time_m], list):
        return random.choice(timelist[time_h][time_m])
    else:
        time = timelist[time_h][time_m]
        return random.choice(timelist[time[0]][time[1]])

# Calling PapirusTextPos this way will mean nothing is written to the screen by default
text = PapirusTextPos(False)

# Application Enter
print("Building times list...", end=" ")
# text.AddText("Building times list...", end=" ")
time_list = buildTimeList()
print("Done")
# text.AddText("Done")

# creating a bool value which checks if clock is running
running = True

# keep clock running till running is true
while running:

    # print("Getting current time...", end=" ")
    time = dt.time(dt.now())
    quote = getTimeQuote(time_list, time)
    # print("Done\n")

    # Write text to the screen at selected point, with an Id
    # Nothing will show on the screen
    text.AddText(f"{quote[2]}\n", 1, 1, 12, Id="Start" )
    print(f"{quote[2]}\n")

    # Add another line of text, at the default location
    # Nothing will show on the screen
    text.AddText(f"{quote[4]}, {quote[3]}", 10, 88, 10, Id="Quote")
    print(f"{quote[4]}, {quote[3]}")

    # Now display BOTH lines on the screen
    text.WriteAll()

    clock.sleep(30)

    # if event is of type quit then set
    # running bool to false
    # if this or that
    #    running = False

    os.system("clear")
    screen.partial_update()

# X set up loop

# X wait 60 seconds then run again

# Have starter I Love You Message or picture up for x seconds - JenLitClock

# later - poll for button press

# add shutdown

# maybe add photo

# Variable to keep the main loop running
