
nums = []
while True:
    number = input("Enter a number (or Enter to quit): ")
    if number == "":
        break
    nums.append(number)
if nums:
    print("Smallest:", min(nums))
    print("Largest:", max(nums))