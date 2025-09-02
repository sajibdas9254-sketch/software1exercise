talents = int(input("the number of talents:"))
pounds = int(input("the number of pounds:"))
lots = int(input("the number of lots:"))
total_lots = talents * 20 * 32 + pounds * 32 + lots
total_grams = total_lots * 13.3
kilograms = int(total_grams // 1000)
grams = total_grams % 1000
print(f" The weight in modern units is {kilograms} kilograms and {grams:.2f} grams.")