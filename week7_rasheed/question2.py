def upper_lower(string):
    upper = 0
    lower = 0
    
    for char in string:
        if char.isupper():
            upper += 1
        elif char.islower():
            lower += 1
    
    return {"Uppercase": upper, "Lowercase": lower}

# Example
input_string = "Testing, Testing, Knock Knock."
numbers = upper_lower(input_string)
print(f"Uppercase letters: {numbers['Uppercase']}")
print(f"Lowercase letters: {numbers['Lowercase']}")