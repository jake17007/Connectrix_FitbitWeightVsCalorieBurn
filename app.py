from __future__ import division
from matplotlib.dates import date2num
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import datetime as dt
import sys, json, pylab, mpld3


# Receive the data passed from runApp.js
data = json.load(sys.stdin)


# Parse the data for calories and weight
fitbitData = data[10]['fitbit']

# calories
caloriesTimeSeries = fitbitData[0]['activityTimeSeries-calories']
caloriesData = caloriesTimeSeries[0]['activities-calories']
caloriesDates_string = [day['dateTime'] for day in caloriesData]
caloriesDates_dt = [dt.datetime.strptime(date, "%Y-%m-%d").date() for date in caloriesDates_string]
caloriesValues = [day['value'] for day in caloriesData]

# weight
weightTimeSeries = fitbitData[1]['bodyTimeSeries-weight']
weightData = weightTimeSeries[0]['body-weight']
weightDates_string = [day['dateTime'] for day in weightData]
weightDates_dt = [dt.datetime.strptime(date, "%Y-%m-%d").date() for date in weightDates_string]
weightValues = [round(float(day['value']) * 2.2, 2) for day in weightData] # Converting to Lbs.

# Plot the calories graph and convert to HTML
plt.plot(caloriesDates_dt, caloriesValues, '-o')
plt.xlabel('Date')
plt.ylabel('Calories')
plt.title('Calories Burned')
fig = plt.gcf()
html_calories = mpld3.fig_to_html(fig)
plt.close()

# Plot the weight graph and convert to HTML
plt.plot(weightDates_dt, weightValues, '-o')
plt.xlabel('Date')
plt.ylabel('Lbs.')
plt.title('Weight')
fig = plt.gcf()
html_weight = mpld3.fig_to_html(fig)

# Combine the two graphs
html = '<div>' + html_calories + '</div><br><div>' + html_weight + '</div>'

# Output
print(json.dumps({'html': html}))

# calores data <- Parse calories
# weight data <- Parse weight
# create the graph
# print
