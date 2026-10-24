# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 Assignment 5

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }
# missing foods
for name, food in food_dict.items():
    if food == '':
        new_food = input(f"What is {name}'s favorite food? ")
        food_dict[name] = new_food

# print new Dict
print("Here are the favorite foods:")
for key, value in food_dict.items():
    print(f"{key}'s favorite food is {value}")