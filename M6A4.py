# Name: Javar Wright
# Student: 1096440
# Section: 07
# Module 6 Assignment 4

def show_messages(messages_list):
    while messages_list:
        popped_message = messages_list.pop()
        print(popped_message)

my_messages = []

while True:
    target = input("What is the next message? (type 'q' to quit)")
    if target == 'q':
        break
    my_messages.append(target)

print("First time calling function")
show_messages(my_messages[:])
print("Second time calling function")
show_messages(my_messages)
