# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:41:43 2024

@author: HP
"""

# Ex_2_Write a program that prints whether an integer 
# is in between 1000 and 2000. If it is not, print
# whether it is lower than 1000 or higher than 2000.

number = int(input("Enter an integer: "))

if number >= 1000 and number <= 2000:
  print("This number is between 1000 and 2000")
elif number < 1000:
  print("This number is lower than 1000")
else:
  print("This number is higher than 2000")