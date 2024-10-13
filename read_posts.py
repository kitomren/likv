######################################################################################
# File: read_posts.py
# Description: open files and read cost data from csv file
# Version: 0.2 October 13th 2024
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
        if line_count == 0:
            print(f'First line, {": ".join(row)}')
            line_count += 1
        else:
            print(f'Cost text: {row[0]},\t\t\tAmount: {row[1]}')
            line_count += 1

    print(f'Processed {line_count} lines.')

csv_file.close()
