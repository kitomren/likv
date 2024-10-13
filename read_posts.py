######################################################################################
# File: read_posts.py
# Description: open files and read cost data from file
# Version: 0.1 October 13th 2024
# Author: Kjell Inge Tomren, kitomren@gmail.com
# Project likv with Python
#
#
######################################################################################
with open("simple_cost_budget.data", mode="r") as file:
  for (line) in file:
        print( line )

file.close()

