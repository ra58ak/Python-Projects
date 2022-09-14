# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1.upper() + name2.upper()


true_total = 0
love_total = 0

true_total+= name.count("T")
true_total+= name.count("R")
true_total+= name.count("U")
true_total+= name.count("E")

love_total += name.count("L")
love_total += name.count("O")
love_total += name.count("V")
love_total += name.count("E")


total = int(str(true_total)+ str(love_total))


if total < 10 or total > 90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif total <= 50 and total >= 40:
    print(f"Your score is {total}, you are alright together.")
else: 
    print(f"Your score is {total}.")