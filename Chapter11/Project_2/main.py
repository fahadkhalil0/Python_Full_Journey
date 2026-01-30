#Guess The Number Game 
#Imported the Random Module to give the numbers randomly.

import random
n = random.randint(1,100)
a = -1
guessess = 0 

# while( a!= n):
#     a = int(input("Guess The Number Please"))
#     if (a > n):
#         print("Enter Lower Number Pls")
#         guessess += 1
#     elif(a < n):
#         print("Enter Higher Number Pls")
#         guessess += 1
# print(f"You Guessed the number {n} correctly in {guessess} attempts ")


# same logic using for loop
for i in range(1,101):
    a = int(input("Guess The Number Please : "))
    if (a > n):
        print("Enter Lower Number Pls")
        guessess += 1
    elif(a < n):
        print("Enter Higher Number Pls")
        guessess += 1
    else:
        print(f"You Guessed the number {n} correctly in {guessess} attempts ")
        break