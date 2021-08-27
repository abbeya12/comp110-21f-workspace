"""numeric operators, type conversion, and string concatenation practice."""

__author__ = "730397724"

"""declare variable and have input for the number, but make sure there is a version for both int and str"""
"""print function can only print strings so when doing the expression convert it to string to have it print"""

str_left_hand: str = input("Left-hand side: ")
str_right_hand: str = input("Right-hand side: ")

int_left_hand: int = int(str_left_hand)
int_right_hand: int = int(str_right_hand)

print(str_left_hand + " ** " + str_right_hand + " is " + (str(int_left_hand ** int_right_hand)))
print(str_left_hand + " / " + str_right_hand + " is " + (str(int_left_hand / int_right_hand)))
print(str_left_hand + " // " + str_right_hand + " is " + (str(int_left_hand // int_right_hand)))
print(str_left_hand + " % " + str_right_hand + " is " + (str(int_left_hand % int_right_hand)))
