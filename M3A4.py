# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 3 Assignment 4

cy_int = int (input("What year is it now? "))
born_int = int (input("What year were you born? "))

age_int = cy_int - born_int
if (age_int % 2) == 0 and age_int < 50:
   print("This will be a great year")
elif(age_int % 2) != 0 and age_int < 50:
   print( "This year will be tough")
elif age_int == 50:
   print("The future is unclear")
else:
   print("Death will come for you soon")