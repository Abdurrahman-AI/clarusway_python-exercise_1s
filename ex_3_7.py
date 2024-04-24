# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 20:11:05 2024

@author: HP
"""

# Ex_7

# Write a program that gives the user a basic test with three questions. 
# If they have a question wrong stop the quiz, if they have it right give 
# them the next question.

questions = [
    ("What is 2 * 2?", "4"),
    ("What is 6 / 3?", "2"),
    ("What is 9 * 9?", "81")
]

question, answer = questions.pop(0)
user_answer = input(question)
if user_answer == answer:
    print("That is correct!\n")
    question, answer = questions.pop(0)
    user_answer = input(question)
    if user_answer == answer:
        print("That is also correct!\n")
        question, answer = questions.pop(0)
        user_answer = input(question)
        if user_answer == answer:
            print("Correct! You passed the test!")
        else:
            print("That is false!You failed the test!")
    else:
        print("That is false!You failed the test!")
else:
    print("That is false!You failed the test!")

