def remove_odd_numbers(numbers):
    new_list = []
    for num in numbers:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
def main():
    original_list = [1, 4, 7, 10, 15, 20, 23]
    filtered_list = remove_odd_numbers(original_list)

    print("Original list:", original_list)
    print("List with odd numbers removed:", filtered_list)

main()