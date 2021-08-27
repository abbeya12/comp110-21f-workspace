"""relational operators, type conversion, bools, INDEPENDENTLY!"""

__author__ = "730397724"

str_left_hand: str = input("Left-hand side: ")
str_right_hand: str = input("Right-hand side: ")

int_left_hand: int = int(str_left_hand)
int_right_hand: int = int(str_right_hand)

print(str_left_hand + " < " + str_right_hand + " is " + (str(int_left_hand < int_right_hand)))
print(str_left_hand + " >= " + str_right_hand + " is " + (str(int_left_hand >= int_right_hand)))
print(str_left_hand + " == " + str_right_hand + " is " + (str(int_left_hand == int_right_hand)))
print(str_left_hand + " != " + str_right_hand + " is " + (str(int_left_hand != int_right_hand)))