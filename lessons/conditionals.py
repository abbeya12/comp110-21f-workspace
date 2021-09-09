"""AN EXAMPLE of if else conditional statements for dynamic control flow in programs."""

SECRET: int = 3
"""an all caps variable is all caps and will never change,, so the program knows that it wont change"""

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!")
    """we are testing to see if the /guess/ is equal to the secret number, bools statement"""
    """after u hit enter on an if guess statement it makes an indent of what happens when it is true (one level indent follows after that if statement"""
    print("Have a wonderful day!!!")
else:
    print("Sorry, you guessed incorrectly :(")
    if guess > SECRET:
        print("You guessed too high!")
    else:
        print("You guessed too low!")
    """everything under /else/ indent happens when the guess doesnt match"""

print("Game over.")