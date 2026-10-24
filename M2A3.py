# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 2 Assignment 3

start_int = int(input("What is the start of your slice? "))
end_int = int(input("What is the end of your slice? "))

uber_list = list(range(100,201, 2))
data_list = uber_list[start_int:end_int]
# we need to tighten up on len()
total_int = 0
for num in data_list:
    total_int = total_int + num
print(f"Your slice contains {len(data_list)} values and has an average value of {total_int/len(data_list)}")





