import random

num = random.randint(1, 10)
guess = int(input("Guess a number (1-10): "))
while True:

    if num < guess:
        print("Too high")
        guess = int(input("Guess a number (1-10): "))
    elif num > guess:
        print("Too low")
        guess = int(input("Guess a number (1-10): "))
    else:
        print("Correct")
        break