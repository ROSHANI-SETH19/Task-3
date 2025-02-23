def find_second_largest(numbers):
    if len(numbers) < 2:
        return None
    numbers = list(set(numbers))  # Remove duplicates
    numbers.remove(max(numbers))
    if not numbers:
        return None
    return max(numbers)

# Example usage:
numbers = [4, 2, 9, 6, 5, 1, 8, 3, 7]
print(find_second_largest(numbers))  # Output: 8