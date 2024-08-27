def random_number(number, start, end):
    if start <= number <= end:
        return f"Yes, {number} is between {start} and {end}."
    else:
        return f"No, {number} is not between {start} and {end}."


print(random_number(34, 4, 50))  
print(random_number(15, 1, 10))  
