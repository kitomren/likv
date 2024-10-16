######################################################################################
# File: read_posts.py
# Description: open files and read cost data from csv file
# Version: 0.4 October 16th 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project: likv with Python
#
#
######################################################################################
import csv 

with open('simple_cost_budget.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if line_count == 0 or line_count == 1:
            print(f'Comment line, {": ".join(row)}')
            line_count += 1
        else:
            day = int(row[0])
            amount = float(row[2])
            print(f'Day of month: {day} \ttext: {row[1]}, Amount: {amount}')
            line_count += 1

    print(f'Processed {line_count} lines.')

csv_file.close()
