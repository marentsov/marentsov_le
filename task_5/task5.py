def analyze_numbers(numbers):
    # Уникальные числа
    unique_nums_count = len(set(numbers))

    # Второе по величине число
    unique_numbers = sorted(set(numbers), reverse=True)
    second_largest = unique_numbers[1] if len(unique_numbers) > 1 else None

    # Числа, делящиеся на 3
    divisible_by_3 = [num for num in numbers if num % 3 == 0]

    data = {
        'unique_nums_count': unique_nums_count,
        'second_largest': second_largest,
        'divisible_by_3': divisible_by_3
    }
    return data



# Test data

num_list = [10, 20, 30, 40, 50, 30, 20]

data = analyze_numbers(num_list)
print("Уникальные числа:", data['unique_nums_count'])
print("Второе по величине число:", data['second_largest'])
print("Числа, делящиеся на 3:", data['divisible_by_3'])