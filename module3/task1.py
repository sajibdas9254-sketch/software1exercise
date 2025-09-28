zander_length = float(input("Enter the length of the zander in centimeters: "))
if zander_length < 42:
    print("The zander does not meet the size limit. \nPlease release the fish back into the lake.")
    missing_cm = 42 - zander_length
    print(f"The fish was {missing_cm:0.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")