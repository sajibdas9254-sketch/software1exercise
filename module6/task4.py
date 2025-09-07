def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def main():
    my_numbers = [3, 7, 2, 10, 5]
    result = sum_list(my_numbers)
    print("sum of the list:", result)
main()