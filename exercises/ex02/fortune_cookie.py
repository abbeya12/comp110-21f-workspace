"""Program that outputs one of at least four random, good fortunes."""

__author__ = "ENTER YOUR 9-DIGIT PID HERE"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint, random
number = random

print("Your fortune cookie says...")
if number == 1:
    print("The sun shines brightly on your future, and you will be smiling.")
else:
    print("This is another filler fortune.")
