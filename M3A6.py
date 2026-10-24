# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 3 Assignment 6

name_str = input("What is the student name? ")
num_int = int(input("What is their score? "))
if num_int >= 90:
    print(f"{name_str} earned an A")
elif num_int >= 80:
    print(f"{name_str} earned a B")
elif num_int >= 70:
    print(f"{name_str} earned a C")
elif num_int >= 60:
    print(f"{name_str} earned a D")
else:
    print(f"{name_str} earned an F")
