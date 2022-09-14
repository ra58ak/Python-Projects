#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tip_percent = int(input("How much tip would you like to give? 10, 12, or 15? "))
num_people = int(input("How many people to split the bill? "))

tip = tip_percent/100
tip_with_bill = tip * bill
total_bill = tip_with_bill + bill
bill_split = total_bill/num_people
each_person_should_pay = "{:.2f}".format(bill_split)
print(f"Each person should pay: {each_person_should_pay}")