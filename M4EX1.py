# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 Extra 1

cities_list = []
#name:str, pop:int, state:str, teams:list
cities_list.append({'name': 'Toronto', 'pop': 2794356, 'state': 'Ontario', 'teams': ['Bluejays', 'Raptors']})
cities_list.append({'name': 'Los Angeles', 'pop': 3898747, 'state': 'California', 'teams': ['Lakers', 'Dodgers', 'Clippers', 'Kings', 'Rams', 'Chargers', 'Sparks']})
cities_list.append({'name': 'Chicago', 'pop': 2746388, 'state': 'Illinois', 'teams': ['Cubs', 'Bulls', "White Sox"]})

team = input("What is your favorite team? ")
#for loop
for city in cities_list:
    if team in city["teams"]:
        print(f"If you like the {team} you should move to {city['name']}.")