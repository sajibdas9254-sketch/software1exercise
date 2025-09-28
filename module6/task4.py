def sum_of_list(integers):
    total = 0
    for i in integers:
        total = i + total
    return total
nums = [5 , 5, 5]
sum = sum_of_list(nums)
print(f"The sum of the numbers in the list is: {sum}")