# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 2 Assignment 1


#how do i code the favorite game Input?
first_fav = input("What is your favorite game? ")
Second_fav = input("What is your second favorite game? ")
third_fav = input("What is your third favorite game? ")

g_list = []

g_list.append(first_fav)
g_list.append(Second_fav)
g_list.append(third_fav)



#now to print the output using pop()
first_fav = g_list.pop()
print(f"One of your favorite games is {first_fav.title()}")
Second_fav = g_list.pop()
print(f"One of your favorite games is {Second_fav.title()}")
third_fav = g_list.pop()
print(f"One of your favorite games is {third_fav.title()}")