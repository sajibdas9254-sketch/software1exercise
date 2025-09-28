def gallons_to_liters(volume):
    lit = volume * 3.785
    return lit
prompt = "Enter a volume in American gallons (negative value to quit): "
user = int(input(prompt))
while True:
    if user < 0:
        print("Program finished.")
        break
    converted = gallons_to_liters(user)
    print(f"{user:0.1f} American gallons is {converted:0.2f} liters.")
    user = float(input(prompt))