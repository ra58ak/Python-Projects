# 🚨 Don't change the code below 👇
from ftplib import parse229


year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year%4 == 0:
    if year%100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else: 
            print("Not leap year")
    else:
        print("Not leap year")
else:
    print("Not leap year")