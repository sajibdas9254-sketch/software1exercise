numbers = []
while True:
    entry = input("Enter a number (or press Enter to quit): ")
    if entry == "":
        break
    else:
        try:
            numbers.append(int(entry))
        except ValueError:
            print("Please enter a valid number.")
numbers.sort(reverse=True)
print("Five greatest numbers (in descending order):")
for i in range(min(5, len(numbers))):
    print(numbers[i])