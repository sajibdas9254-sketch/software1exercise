import random
def roll_dice(sides):
    num = random.randint(1,sides)
    return num
user = int(input())
rolled = roll_dice(user)
store = []
while rolled != user:
    store.append(rolled)
    rolled = roll_dice(user)
store.append(rolled)
for i in store:
    print(i)