# Snake Water Gun Game
'''
snake = -1
water = 1
gun = 0
'''
#Program staring
import random
computer  = random.choice([1,-1,0])

youStr = input("Enter your choice : ")

youDict = { "s":1, "w":-1, "g":0}
revDict = {1: "snake", -1: "water", 0 : "gun"}

You = youDict[youStr] #Input from user will be extract the data from dictionary.

#print which number you choose
print(f"You chose {revDict[You]}, and Computer chose {revDict[computer]}")

if (computer == You):
    print("It's a tie!")
else:
    if(computer == -1 and You == 1):
        print("You Win!")
    elif(computer == -1 and You == 0):
        print("You Lose!")
    elif(computer == 1 and You == -1):
        print("You Lose!")
    elif(computer == 1 and You == 0):
        print("You Win!")
    elif(computer == 0 and You == -1):
        print("You Win!")
    elif(computer == 0 and You == 1):
        print("You Lose!")
    else:
        print("Invalid input, please try again.")