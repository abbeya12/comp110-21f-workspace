"""an example of a while loop statement."""

counter: int = 0
"""prepare a variable, and make it zero so it can count up"""
maximum: int = int(input("Count up to, but not including what?"))

while counter < 10:
    counter_squared: int = counter ** 2
    print("The square of " + str(counter) + " is " + str(counter_squared))
    counter = counter + 1
"""while counter is less than ten, print the number but then add one. then if that number is less than 10 again, add another until it is not less than 10. """


print("Done!")