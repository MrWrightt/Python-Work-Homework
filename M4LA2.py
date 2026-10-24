# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 L Assignment 2


city_list = {'Paris' : 'France', 'London' : 'United Kingdom', 'New York' : 'USA'}
city_list['Detroit'] = 'USA' # adding to dictionary
city_list['London'] = 'Great Britain' # adding but changing outcome

tmp_var = input("What city would you like to learn about? ")

print(f"The city of {tmp_var} is in the country of {city_list.get(tmp_var, "not found")}")
