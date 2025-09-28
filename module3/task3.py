gender = input("Enter biological gender (male/female): ")
hemoglobin = float(input("Enter hemoglobin value (g/l): "))

if (gender.lower() == 'female' and hemoglobin < 117) or (gender.lower() == 'male' and hemoglobin < 134):
    print("Your hemoglobin is low.")
elif (gender.lower() == 'female' and hemoglobin > 155) or (gender.lower() == 'male' and hemoglobin > 167):
    print("Your hemoglobin is high.")
elif (gender.lower()!='male' and gender.lower()!='female'):
    print("Invalid gender.")
else:
    print("Your hemoglobin is normal.")