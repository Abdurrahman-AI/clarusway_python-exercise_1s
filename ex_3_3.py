# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:46:42 2024

@author: HP
"""
# Ex_3_3

# Write a program that prints the sum of 3 given numbers, but if 
# all 3 numbers are the same, it should print 4 times the sum of the 3 numbers.

first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
third_number = int(input("Enter the third number: "))

# Calculate the sum
sum_of_numbers = first_number + second_number + third_number

# Check if all numbers are the same (uses short-circuit evaluation)
if first_number == second_number == third_number:
  # Print message for all same numbers and calculate multiplied sum
  print("These numbers are the same!")
  print(f"The sum of these numbers is {sum_of_numbers}")
  print(f"Multiplied by 4 this becomes {sum_of_numbers * 4}")
else:
  # Print message for regular sum
  print(f"The sum of these numbers is {sum_of_numbers}")