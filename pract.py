banned = ['andrew', 'Tray', 'Luke']
user = str(input("What is your Name? "))
if user not in banned:
    print(f"Welcome to Footprnt {user}!!!")
else:
    print("naw kick rocks")