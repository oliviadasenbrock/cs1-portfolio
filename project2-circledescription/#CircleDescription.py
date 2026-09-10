#CircleDescription

"""This program tells you my name, major, and hometown and then
calculates the area and circumference of a circle as long as the
user knows the radius"""

name = "Olivia Dasenbrock."
print("My name is", name)

major = "Civil Engineering major."
print("I am a", major)

hometown = "Teutopolis, IL."
print("I am from", hometown)

print()

print("I will find the circumference and area of a circle for you.")

print()

radius = float(input("Input your circle radius:"))

print()

pi = 3.1415926536

circumference = 2 * pi * radius

area = pi * radius ** 2

print("The circumference is", circumference)

print("The area is", area)