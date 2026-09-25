#RightTriangles.py


"""This program reads three integers from the keyboard amd determines whether
they could be the sides of a right triangle."""

print("Input three positive integers representing sides of a triangle.")

a = int(input("Side 1:"))

b = int(input("Side 2:"))

c = int(input("Side 3:"))

if a <= 0:
    print("Error: Side 1 must be positive!")
    
elif  b <= 0:
    print("Error: Side 2 must be positive!")
        
elif c <= 0:
    print("Error: Side 3 must be positive!")
    
elif (a ** 2) + (b ** 2) == (c ** 2):
    print(a, ",", b, "and", c, "could be sides of a right triangle.")
    
elif (b ** 2) + (c ** 2) == (a ** 2):
    print(a, ",", b, "and", c, "could be sides of a right triangle.")
    
elif (c ** 2) + (a ** 2) == (b ** 2):
    print(a, ",", b, "and", c, "could be sides of a right triangle.")
    

    
else:
    print(a, ",", b, "and", c, "could NOT be sides of a right triangle.")
    