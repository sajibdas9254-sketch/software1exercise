length = float(input("Enter length in inches (negative value to quit): "))
while length >= 0:
    print(f"{length:0.1f} inches is {length * 2.54:0.2f} centimeters")
    length = float(input("Enter length in inches (negative value to quit): "))
print("Program ended.")