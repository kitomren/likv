######################################################################################
# File: read_posts.py
# Description: open files and read cost data from csv file
# Version: 0.5 October 19th 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project: likv with Python
#
#
######################################################################################
import csv 
from datetime import datetime

with open('simple_cost_budget.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0 or line_count == 1:
            print(f'Comment line, {": ".join(row)}')
            line_count += 1
        else:
            text = row[0]
            number = int(row[1])
#            date = convert-to-internal(row[2])
            time_obj=datetime.strptime(row[2],'%Y/%m/%d')
            date = time_obj.strftime("%A %B %d %Y")
            print(f'{text} Antall: {number} Dato: {date}')
            line_count += 1

    print(f'Processed {line_count} lines.')

csv_file.close()
