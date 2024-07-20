# To print the youngest age

def find_youngest_age():
    ages = []
    for i in range(4):
        age = int(input(f"Enter age for person {i + 1}: "))
        ages.append(age)

    youngest_age = min(ages)
    return youngest_age


youngest = find_youngest_age()
print(f"The youngest age is: {youngest}")