import random

rand = random.randint(1,10)
chance = 3


def startGame():
    global rand
    global chance
    

    for i in range(chance , 0, -1):
        choice = int(input("choose a number from 0 to 10: "))
        if (choice == rand):
            print("You Won!!!")
            break
        elif (choice > rand):
            print(f" {choice} is greater. you still have {i - 1} attempts")
        else:
            print(f" {choice} is smaller. you still have {i - 1} attempts")
    else:
        print(f"Game Over. The number was {rand}")

startGame()