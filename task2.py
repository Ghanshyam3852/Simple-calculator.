# Guess the number

import random

target = random.randint(1,100)

while True:
    userchoice =input ("guess the target or Quit (Q): ")
    if (userchoice == "Q"):
        break

    userchoice = int (userchoice)
    if(userchoice == target):
        print("sucess : correct Guess!")
        break
    elif(userchoice < target):
        print(" Too high! Try again.")
    else:
        print("Too low! Try again.")
     
print("------GAME OVER-------")

