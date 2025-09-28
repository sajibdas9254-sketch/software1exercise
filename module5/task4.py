#Create an list
name = []
#Ask input from user for 5 times
for i in range (5):
    names = input("Enter the name of a city: ")
    #Add the input from user to the list
    name.append(names)
print("\n\nThe cities you entered: ")
#Print the list of cities serially
for i in name:
    print(i)