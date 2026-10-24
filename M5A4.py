# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 5 Assignment 4


orders_list = ['pastrami', 'turkey', 'pastrami', 'ham', 'turkey']

finished_list = []

while orders_list:
    current_sandwich = orders_list.pop()
    print(f"I made your {current_sandwich}")
    finished_list.append(current_sandwich)


print("Here are all the sandwiches I made:")
for sandwich in finished_list:
    print(sandwich)