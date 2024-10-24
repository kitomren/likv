######################################################################################
# File: read_posts.py
# Description: open files and read cost data from csv file
# Version: 0.7777777 October 24 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project: likv with Python
#
# format: text; number; year/month/day; periode_type; periode_delta; fix; amount_in; amount_out
######################################################################################
import csv 
from datetime import datetime

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
            print(f'{text} Antall: {number} Dato: {date} Periode type: {periode_type} pd: {periode_delta} Fix: {fix} Inn: {amount_in} Ut: {amount_out}')
            line_count += 1

    print(f'Processed {line_count} lines.')

csv_file.close()
