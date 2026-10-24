# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 2 Assignment 2


g_list = ['Mortal Kombat', 'Contra', 'Streets Of Rage', 'Shinobi', 'Sonic', 'Phantasy Star']


print("Here are the top Sega games:")
for g in g_list:
    print(f"{g.title()}")

g_removed = str(input("Which one do you think should be removed? "))

g_list.remove(g_removed)

print("Here are the new top Sega games:")
for g in g_list:
    print(g)