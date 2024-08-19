def count_upper_lower(Cathedral):

    upper_count = 0
    lower_count = 0
    
    for char in Cathedral:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
    
    return upper_count, lower_count

result = count_upper_lower("CaThedraL")
print(f"Uppercase letters: {result[0]}, Lowercase letters: {result[1]}")
