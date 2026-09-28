#Factors.py


"""This program prompts the user for the values of three input
variables and outputs the factors of that variable."""


start = int(input("Enter starting number:"))

incr = int(input("Enter increment:"))

numrows = int(input("Enter number of rows:"))

print()

print("Number \t Factors")

row = 0

while row < numrows:

    print(start, "\t    \t", end="",)
    
    factor = 1
    while factor <= start:
        if start % factor == 0:
            print(factor, "\t", end="")
        factor = factor + 1

    print()
    row = row + 1
    start = start + incr
