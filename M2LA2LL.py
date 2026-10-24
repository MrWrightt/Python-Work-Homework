# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 2 Lecture Assignment 2 loop

games = ['Zelda', 'Mario', 'Halo']
print(games)

print("Now each on their own line")
for game in games:
    print(f"This game is {game.title()}")
    print("one time through the loop")


numbs = list(range(1,5))
for n in numbs:
    print(f" the number {n} doubled is {n * 2}")


big_num = range(73,212,4)
total = 0
for n in big_num:
    total += n
    print(f"The total is {total}, the number of item is {len(big_num)}, and the average is {total / len(big_num)}")


    print("The program is over" )
