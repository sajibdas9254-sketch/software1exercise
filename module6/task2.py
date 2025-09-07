import random

def roll_dice(sides):
    return random.randint(1, sides)

def main():
    sides = int(input("Enter the number of sides: "))
    max_number = sides
    result = 0
    while result != max_number:
        result = roll_dice(sides)
        print("You rolled:", result)

main()