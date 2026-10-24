# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 Extra 2

food_dict = {'Jim': 'Tacos',
             'Bob': 'Burgers',
             'Janelle': '',
             'Lisa': 'Pizza',
             'Thomas': '',
             'Yolanda': '',
             'Finn': 'Bread',
             }
for name, food in food_dict.items():
    if food == '':
        new_food = input(f"What is {name}'s favorite food? ")
        food_dict[name] = new_food

counts = {}
# find popular food
for  food in food_dict.values():
    if food in counts:
        counts[food] = counts[food] + 1
    else:
        counts[food] = 1

popular_food = ""
highest = 0
for food in counts:
    if counts[food] > highest:
        highest = counts[food]
        popular_food = food

# print new Dict
print("Here are the favorite foods:")
for key, value in food_dict.items():
    print(f"{key}'s favorite food is {value}")

print(f"The most popular food is {popular_food}")