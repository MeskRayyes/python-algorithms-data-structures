
def find_duplicate(numbers):
    for i in range(len(numbers)):
        for j in range(i):
            if numbers[i] == numbers[j]:
                return numbers[i]

    return None


numbers = [4, 2, 7, 2, 9, 4]

result = find_duplicate(numbers)

print("Input:", numbers)
print("First duplicate:", result)
