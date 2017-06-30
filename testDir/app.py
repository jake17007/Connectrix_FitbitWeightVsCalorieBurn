from __future__ import division
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
import sys, json, pylab, mpld3


with open('./data.json') as data_file:
    data = json.load(data_file)
# Receive the data passed from runApp.js
#data = json.load(sys.stdin)


# Parse the data for calories and weight
fitbitData = data[0]['fitbit']

# calories
caloriesTimeSeries = fitbitData[0]['activityTimeSeries-calories']
caloriesData = caloriesTimeSeries[0]['activities-calories']
caloriesDates_string = [day['dateTime'] for day in caloriesData]
caloriesDates_dt = [dt.datetime.strptime(date, "%Y-%m-%d").date() for date in caloriesDates_string]
caloriesValues = [day['value'] for day in caloriesData]

# weight
weightTimeSeries = fitbitData[1]['bodyTimeSeries-weight']
weightData = weightTimeSeries[0]['body-weight']
weightDates = [day['dateTime'] for day in weightData]
weightValues = [day['value'] for day in weightData]


# Plot the graph
plt.plot(caloriesDates_dt, caloriesValues, '-o')
fig = plt.gcf()

# Convert the plot to HTML
html = mpld3.fig_to_html(fig)

# Output
print(json.dumps({'html': html}))

# calores data <- Parse calories
# weight data <- Parse weight
# create the graph
# print
