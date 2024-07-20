#Write a function that accepts the age of 4 people and displays the youngest.
def find_youngest(age):
    youngest = min(age)
    print(f"The youngest age is {youngest}")

# Accept ages of 4 people
age = [int(input(f"Enter age of person {i+1}: ")) for i in range(4)]
find_youngest(age)