def filter_even_numbers(integers):
    even = []
    for i in integers:
        if i % 2 == 0:
            even.append(i)
    return even

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evn = filter_even_numbers(nums)
print(f"Original list: {nums}")
print(f"List with even numbers only: {evn}")