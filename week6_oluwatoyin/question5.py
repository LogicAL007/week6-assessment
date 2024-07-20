# To print the oldest age
def find_oldest_age():
    ages = []
    for i in range(4):
        age = int(input(f"Enter age for person {i + 1}: "))
        ages.append(age)

    oldest_age = max(ages)
    return oldest_age


oldest = find_oldest_age()
print(f"The oldest age is: {oldest}")
