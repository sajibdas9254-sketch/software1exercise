while True:
    inches = float(input("Enter length in inches: "))
    if inches < 0:
        print("Program ended.")
        break
    else:
        centimeters = inches * 2.54
        print(f"{inches} inches is {centimeters:.2f} centimeters.")