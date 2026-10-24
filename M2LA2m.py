# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 2 Lecture Assignment 2 More


mylist = [50,50]
mylist[0] = 20
print(mylist)

mytuple = (50, 50)
print(mytuple)
#mytuple[0] = 25

for x in mytuple:
    print(f"The value is {x}")

main_char = ['link', 'mario', 'zelda', 'toad', 'luigi', 'kirby', 'yoshi', 'gannon']
print(main_char)
new_char = main_char[:]
del (new_char[0])

for guy in new_char[2:4]:
    print(f"This charater name is {guy}")

print("the end of program")