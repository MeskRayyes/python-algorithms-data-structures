
def find_duplicate(numbers):
    seen = set()

    for number in numbers:
        if number in seen:
            return number

        seen.add(number)

    return None


numbers = [4, 2, 7, 2, 9, 4]

result = find_duplicate(numbers)

print("Input:", numbers)
print("First duplicate:", result)
