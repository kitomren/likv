######################################################################################
# File: date_example.py
# Description: write descripion!
# Version: 0.3 October 28th 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project: likv with Python
#
#
######################################################################################
# from sys import argv
import datetime 

# import locale
# locale.setlocale(locale.LC_ALL, 'nb-NO')
# note to self: får feilmelding på denne på MacBook Pro. 
# Vet ikke om det er koden som er feil eller Macen som ikke har support for norsk. 
# må sjekke dette nærmere.

# class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)

date = datetime.date(2020, 10, 20)
print(date)
today = datetime.date.today() # current date 
print(today)

# next_week = now + 1 week
# one_week = datetime.datetime.timedelta(weeks=1)
# next_week = now + one_week
# date_time = next_week.strftime("%A%d/%B/%Y, %H:%M:%S")
# print("next week:",date_time)

# next_month = now + 1 month

#date_time = now.strftime("%A%d/%B/%Y, %H:%M:%S")
#print("date and time:",date_time)

# next_year = now + 1 year

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
