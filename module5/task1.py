import random
rolls = int(input("How many dice to roll: "))
#make a list to store values to add later
total_rolls = []
#run this loop the times user said
for i in range(rolls):
    a = random.randint(1,6)
    #add the value you get in a to list total_rolls by using append
    total_rolls.append(a)
#print(total_rolls)
result = sum(total_rolls)
print(f"Sum of the dice: {result}")