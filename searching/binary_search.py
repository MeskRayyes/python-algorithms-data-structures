
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1


# Example
numbers = [2, 4, 6, 8, 10, 12, 14]
target = 10

result = binary_search(numbers, target)

print("Numbers:", numbers)
print("Target:", target)
print("Index:", result)
