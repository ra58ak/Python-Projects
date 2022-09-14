import random

print("Welcome to the coin flipper")

coin_flip =  random.randint(0,1)
if coin_flip == 0:
    print("Heads")
else:
    print("Tails")