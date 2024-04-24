# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 21:10:43 2024

@author: HP
"""

# Ex_5

# In a certain tax system, people who earn more have to pay a higher 
# percentage of taxes. For example:
# People earning under €67000 have to pay 24% of all of their earnings to 
# the government in taxes.
# People earning under €97000 have to pay 31% of all of their earnings to 
# the government in taxes.
# People earning more than €97000 have to pay 34% of all of their earnings 
# to the government in taxes.

# Write a program that calculates how much money someone has left after 
# taxes, given their income.


under_67000 = 67000       # Tax thresholds (euros)
under_97000 = 97000


tax_rate_24 = 0.24        # Tax rates
tax_rate_31 = 0.31
tax_rate_34 = 0.34

# Input for income
income = float(input("Enter your income in euros: "))

# Determine tax rate based on income 
if income <= under_67000:
  tax_rate = tax_rate_24
elif income <= under_97000:
  tax_rate = tax_rate_31
else:
  tax_rate = tax_rate_34

# Calculate tax amount and income after tax
tax_amount = income * tax_rate
income_after_tax = income - tax_amount

# Print the result
print(f"Your income after taxes is {income_after_tax:.2f} euros")