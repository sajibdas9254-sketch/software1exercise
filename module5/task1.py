import random

num_dice = int(input("How many dice do you want to roll: "))
total = 0
for i in range(num_dice):
    roll = random.randint(1, 6)
    print(f"Die {i+1}: {roll}")
    total += roll
print("Total sum of dice:", total)