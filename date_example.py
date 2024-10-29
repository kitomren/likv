######################################################################################
# File: date_example.py
# Description: test of date library functions 
# Version: 0.4 October 29th 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project: likv with Python
#
#
######################################################################################
# from sys import argv
import datetime 
from dateutil.relativedelta import relativedelta

# import locale
# locale.setlocale(locale.LC_ALL, 'nb-NO')
# note to self: får feilmelding på denne på MacBook Pro. 
# Vet ikke om det er koden som er feil eller Macen som ikke har support for norsk. 
# må sjekke dette nærmere.

# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

today = datetime.date.today() # current date 
print(today)

# next_week = now + 1 week
delta = relativedelta(weeks=1)
next_date = today + delta
print(next_date)

# next_week = now + one_week
# date_time = next_week.strftime("%A%d/%B/%Y, %H:%M:%S")
# print("next week:",date_time)

# delta = relativedelta(weeks=1,hours=25, day=1, weekday=MO(1))
# next_date = today + delta

# next_month = now + 1 month
delta = relativedelta(months=1)
next_date = today + delta
print(next_date)

# next_year = now + 1 year
delta = relativedelta(years=1)
next_date = today + delta
print(next_date)


# day --> datetime.date(2021, 1, 8)

# deadline --> datetime.date(2021, 2, 8)

#date_time = now.strftime("%A%d/%B/%Y, %H:%M:%S")
#print("date and time:",date_time)

# date_time = now.strftime("%A%d/%B/%Y, %H:%M:%S")
# print("date and time:",date_time)


# year = now.strftime("%Y")
# print("year:", year)

# month = now.strftime("%m")
# print("month:", month)

# day = now.strftime("%d")
# print("day:", day)

# time = now.strftime("%H:%M:%S")
# print("time:", time)

# date_time = now.strftime("%A%d/%B/%Y, %H:%M:%S")
# print("date and time:",date_time)
