# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 L Assignment 3

city_dic1 = {'name' : 'los angeles',
             'pop' : 13000000,
             'state': 'ca',
             'country' : 'usa',
             'teams' : {'dodgers': 'baseball', 'angels' : 'baseball', 'lakers' : 'basketball'}}


for key, value in sorted(city_dic1.items()):
    print(f"{key} - {value}")