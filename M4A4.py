# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 Assignment 4

print("I know Jimmer has three scout badges, what are they?")

#jim's info
guy_dict1 = {
    'name': 'Jimmer',
    'age': 23,
    'scout rank': 'Eagle',
    'scout badges' : []
    }
# badge inputs
fir_b = input("The first badge is: ")
sec_b = input("The second badge is: ")
thr_b = input("The third badge is: ")

guy_dict1['scout badges'].append(fir_b)
guy_dict1['scout badges'].append(sec_b)
guy_dict1['scout badges'].append(thr_b)

print(guy_dict1)