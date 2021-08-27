"""A program to demonstrate user input and variables."""

user_name: str = input("Who are you? ")
""""this menas that the input (name) will then be noted as being the username -- variable name"""
""""variable type = str ... it has to be characters and its being stored as a string"""
""" =  assigning opporator ,,, username is going to be assigned, and whatever follows is what is assigned to variable"""

print("Wow, " + user_name + ", you rock!")
print(user_name + " have a great day!")

"""all of this stack (variables) are happening in the global frame"""
""" output : Wow, abbey, you rock! """
"""only asked for input once, and can be used many times later in program"""