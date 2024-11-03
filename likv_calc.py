######################################################################################
# File: likv_calc.py
# Description: read sorted posts and calculate likv saldo
# Version: 0.1 November 3rd 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project: likv with Python
#
#
######################################################################################
from sys import argv
import csv 
from datetime import *
from dateutil.relativedelta import relativedelta

saldo = 0.0
with open('sorted.data') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if row[0][0] == "#":
#            print(f'Comment line, {row[0][0]}')
            line_count += 1
        else:
            date = row[0]
            text = row[1]
            amount_in = float(row[2])
            amount_out = float(row[3])
            saldo = saldo + amount_in - amount_out
            print(date,";",text,";",amount_in,";",amount_out,";",saldo)
csv_file.close()
