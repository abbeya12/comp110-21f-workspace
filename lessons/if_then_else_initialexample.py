"""Challenge Question #1."""

choice: int = int(input("Enter a number: "))

if choice > 50:
    if choice < 25:
        print("A")
        """A is unreachable which is an issue."""
    else:
        print("B")
else:
    if choice > 75:
        print("C")
        """C is unreachable which is an issue."""
    else:
        print("D")