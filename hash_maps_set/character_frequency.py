
def character_frequency(text):
    frequency = {}

    for character in text:
        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    return frequency


# Example
text = "banana"
result = character_frequency(text)

print("Input:", text)
print("Character Frequency:", result)
