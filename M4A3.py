# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 4 Assignment 3

games_dict = {}
# 3 games
for i in range(3):
    game = input("What is a great game? ")
    system = input("What system can I play that on? ")
    games_dict[game] = system

print("That's too many, let's get rid of one")
# remove game
del_game = input("What game should we remove? ")
if del_game in games_dict:
    del games_dict[del_game]

# print new Dict
print("The new dictionary is:")
for game, system in games_dict.items():
    print(f"You can play {game} on {system}")