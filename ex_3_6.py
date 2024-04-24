# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:03:33 2024

@author: HP
"""

# Ex_3_6

# Write a program that takes a string with a maximum size of 5. 
# Do something different depending on the size of the string:
# 1 Letter: Print the letter 6 times (a = aaaaaa)
# 2 Letters: Switch the position of the letters (at = ta)
# 3 Letters: Move the last letter from the back to the front (Dog = gDo)
# 4 Letters: Print the reverse of the word (Wait = taiW)
# 5 Letters: Print the word divided by t (Brain = Btrtatitn)

string = input("Enter a string with a maximum size of 5: ")

if len(string) == 1:
    print(string * 6)
elif len(string) == 2:
    print(string[1] + string[0])
elif len(string) == 3:
    print(string[2] + string[:2])
elif len(string) == 4:
    print(string[::-1])
elif len(string) == 5:
    print('t'.join(string))
else:
    print("String size exceeds the maximum limit of 5.")
