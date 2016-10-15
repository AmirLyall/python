# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 19:06:42 2016

@author: Amir Lyall
"""
#import packages
import urllib2
import json
import time
from datetime import date, datetime, timedelta
import csv
#open CSV file for data
out = open('temp.csv', 'wb')
writer = csv.writer(out)
#setting up column headers for data to be written - hourly data
writer.writerow(['Hour1', 'Hour2', 'Hour3', 'Hour4', 'Hour5', 'Hour6', 'Hour7', 'Hour8', 'Hour9', 'Hour10', 
                 'Hour11', 'Hour12', 'Hour13', 'Hour14', 'Hour15', 'Hour16', 'Hour17', 'Hour18', 'Hour19', 'Hour20',
                 'Hour21', 'Hour22', 'Hour23', 'Hour24'])
#create list with all dates from start date to today - replace YYYY, MM, DD
start_date=date(YYYY, MM, DD)
day_count=abs((date.today()-start_date).days)
dates=list()
for single_date in (start_date+timedelta(n) for n in range(day_count)):
   day=str(single_date.year)+single_date.strftime('%m')+ single_date.strftime('%d')
   dates.append(day)
#run the JSON for each day - insert YOUR-API-KEY and replace STATE-OR-COUNTRY/CITY with location of interest
for day in dates:
        f = urllib2.urlopen('http://api.wunderground.com/api/YOUR-API-KEY/history_'+day+'/q/STATE-OR-COUNTRY/CITY.json')
        json_string = f.read()
        parsed_json = json.loads(json_string)
#loop for hourly temperatures in Farenheit   
        hours=()
        for i in range(0,23):
           # time.sleep(7)
            temp=parsed_json['history']['observations'][i]['tempi']
            hours.append(temp)
            i=i+1
#writes each row to the csv file
        writer.writerow(hours)
out.close()