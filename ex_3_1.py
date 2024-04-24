# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 19:35:42 2024

@author: HP
"""

# Ex_1_Write a program that tells the user whether a letter is a vowel or not.

vowels = "aeiouAEIOU"

letter = input("Enter a letter: ")

if len(letter) != 1:
  print("Please enter a single letter.")
else:
  if letter in vowels:
    print(f"{letter} is a vowel.")
  else:
    print(f"{letter} is not a vowel.")