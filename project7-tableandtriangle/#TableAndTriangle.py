#TableAndTriangle.py


"""This program asks the user for two integers, number of rows and
number of columns and print a rectangle and triangle of asterisks."""

numrows = int(input("Enter number of rows:"))
numcols = int(input("Enter number of columns:"))

if numrows <= 1:
    print("Number of rows must be greater than zero.")
elif numrows >= 80:
    print("Number of rows must be less than or equal to 80.")
elif numcols <= 1:
    print("Number of columns must be greater than zero.")
elif numcols >= 80:
    print("Number of columns must be less than or equal to 80.")
else:
    print(f"The following rectangle has {numrows} rows and {numcols} columns:")

    for counter in range(numrows): #counter = 0,1,2,....,rows -1 
        for counter2 in range(numcols): #counter = 0,1,2,....,columns -1
            print("*", end = "") #print row times 
        print()
    
    print(f"The following triangle has {numrows} rows:")

    for counter in range(numrows): 
        for counter2 in range(numrows):
            print("*", end = "") 
        numrows -= 1
        print()