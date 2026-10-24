# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 Assignment 2


food_dict = {}

for i in range(3):
    dish = input("What is good to eat? ")
    country = input("What country is that from? ")
    food_dict[dish] = country

tmp_var = str(input("What dish do you like? "))

print(f"{tmp_var} is from {food_dict[tmp_var]}")