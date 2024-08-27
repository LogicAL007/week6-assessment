def count_letters(text):
    upper = 0
    lower = 0
    for char in text:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    return f"Uppercase letters: {upper}, Lowercase letters: {lower}"

print(count_letters("This is Data_Epic"))