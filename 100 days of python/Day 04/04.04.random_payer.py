import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = len(names)
ran_sel = random.randint(0,name-1)
print(f"{names[ran_sel]} is going to buy the meal today!")