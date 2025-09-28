import random
def roll_dice():
    num = random.randint(1,6)
    return num
rolled = roll_dice()
store = []
while rolled != 6:
    store.append(rolled)
    rolled = roll_dice()
store.append(rolled)
for i in store:
    print(i)