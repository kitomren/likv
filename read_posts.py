######################################################################################
# File: read_posts.py
# Description: open file,d read cost data from csv file, generate entries and write to file
# Version: 0.8 October 31 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project: likv with Python
#
# format: text; number; year/month/day; periode_type; periode_delta; fix; amount_in; amount_out
######################################################################################
import csv 
from datetime import *
from dateutil.relativedelta import relativedelta

with open('simple_cost_budget.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if row[0][0] == "#":
#            print(f'Comment line, {row[0][0]}')
            line_count += 1
        else:
            text = row[0]
            number = int(row[1])
#            date = convert-to-internal(row[2])
            time_obj=datetime.strptime(row[2],'%Y/%m/%d')
            date = time_obj.strftime("%A %B %d %Y")
            periode_type = row[3]
            periode_delta = int(row[4])
            fix = row[5]
            amount_in = float(row[6])
            amount_out = float(row[7])

            if ("w" in periode_type):

                print(f'w {text} Antall: {number} Dato: {date} Periode type: {periode_type} pd: {periode_delta} Fix: {fix} Inn: {amount_in} Ut: {amount_out}')
                line_count += 1
            elif ("m" in periode_type):
                print(f'm {text} Antall: {number} Dato: {date} Periode type: {periode_type} pd: {periode_delta} Fix: {fix} Inn: {amount_in} Ut: {amount_out}')
                line_count += 1
            elif ("y" in periode_type):
                print(f'y {text} Antall: {number} Dato: {date} Periode type: {periode_type} pd: {periode_delta} Fix: {fix} Inn: {amount_in} Ut: {amount_out}')
                line_count += 1
            else:
                print("Unknown type of period")

    print(f'Processed {line_count} lines.')

csv_file.close()
