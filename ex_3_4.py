# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:54:13 2024

@author: HP
"""

# Ex_4

# Write a program that finds the largest of 4 numbers.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))
fourth_number = float(input("Enter the fourth number: "))

largest_number = first_number

if second_number > largest_number:
  largest_number = second_number
if third_number > largest_number:
  largest_number = third_number
if fourth_number > largest_number:
  largest_number = fourth_number

print(f"The largest number is {largest_number}")