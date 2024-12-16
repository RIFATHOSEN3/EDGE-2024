def filter_odd(numbers):
    odd_numbers = []
    for num in numbers:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers

sample_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(filter_odd(sample_input))