#Write a function that accepts the age of 4 people and displays the youngest.
def find_youngest(age):
    youngest = min(age)
    print("The youngest age is " + str(youngest))

age = [int(input("Enter age of person {}: ".format(i + 1))) for i in range(4)]
find_youngest(age)