# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 5 Assignment 2

start = int(input("Enter the start of the loop: "))
limit = int(input("Enter the limit of the loop: "))

current = start

while current < limit:
    print(f"The current value is {current}")
    current *= 2

print(f"The last value of current that was less than {limit} was {int(current / 2)}")