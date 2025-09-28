# Taking the inputs and storing the values in the list
number = input("Enter a number: ")
numberlist = []
while number != "":
    number = float(number)
    numberlist.append(number)
    number = input("Enter a number: ")
# Sorting
numberlist.sort(reverse=True)
print("The greatest numbers in descending order:")
#conditions if inputs are less than 5 numbers or more
if len(numberlist)<5:
    for i in numberlist:
        print(i)
else:
    for j in range(0,5):
        print(numberlist[j])