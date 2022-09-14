import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇



# player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
# choice = [rock, paper, scissors]


# if player_choice >= 3 or player_choice < 0:
#     print("You chose an invalid number")
# else:  
#     player_cho = choice[player_choice]
#     print(player_cho)

#     print("Computer Choose")

#     com_choice = len(choice)
#     rad_selec = random.randint(0, com_choice-1)
#     comp_choice = choice[rad_selec]
#     print(comp_choice)

#     if player_cho == rock:
#         if comp_choice == rock:
#             print("It is a drow")
#         elif comp_choice == paper:
#             print("You lose ")
#         else:
#             print("You win!")
#     elif player_cho == paper:
#         if comp_choice == rock:
#             print("You win!")
#         elif comp_choice == paper:
#             print("It is a draw ")
#         else:
#             print("You lose")
#     elif player_cho == scissors:
#         if comp_choice == rock:
#             print("You lose")
#         elif comp_choice == paper:
#             print("You win! ")
#         else:
#             print("It is a draw")game_images = [rock, paper, scissors]

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
print(game_images[user_choice])

computer_choice = random.randint(0, 2)
print("Computer chose:")
print(game_images[computer_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and computer_choice == 2:
  print("You win!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose")
elif computer_choice > user_choice:
  print("You lose")
elif user_choice > computer_choice:
  print("You win!")
elif computer_choice == user_choice:
  print("It's a draw")
