# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 Assignment 1

g_list =[]

first_game = str(input("What is your number 1 favorite PlayStation game? "))
g_list.append(first_game)
second_game = str(input("What is your number 2 favorite PlayStation game? "))
g_list.append(second_game)
third_game = str(input("What is your number 3 favorite PlayStation game? "))
g_list.append(third_game)



for i, game in enumerate(g_list, start=1):
    print(f"Your number {i} favorite game was {game}")