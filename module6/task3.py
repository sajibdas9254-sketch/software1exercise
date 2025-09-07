s
def gallons_to_liters(gallons):
    liters = gallons * 3.78541
    return liters
def main():
    while True:
        gallons = float(input("Enter volume in gallons: "))
        if gallons < 0:
            print("Exiting the program.")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.\n")

main()