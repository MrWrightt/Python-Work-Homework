# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 3 L Assignment 1

age = 20
if age != 21 or age == 19:
    print ("age is 20")

toppings = ['mushrooms', 'onions', 'pineapple', 'peperoni', 'sausage']
request = input("What do you wanton your pizza? ")
if request == 'onions':
   print("yum, onions")
elif request == 'pineapple':
   print("Awesome, i dont care what people think about me anyway")
elif request == 'sausage':
   print("sooo spicy")
elif request in toppings:
   print("Its on the list")
else:
   print("No one loves me, I never get what i want I hate you")