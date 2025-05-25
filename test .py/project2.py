# GUESS THE NUMBER

import random

target = random.randint(1,100)

while True:
    userchoice = input("Guess the target or Quit :")
    if(userchoice == "Quit"):
        break

    userchoice = int(userchoice)
    if(userchoice == target):
        print("sucess : correct Guess !!")
        break
    elif(userchoice < target):
        print("your number was too small.Take a bigger number Guess..")
    else:
        print("your number is too big.Take a smaller number Guess..")


print("______GAME OVER______")