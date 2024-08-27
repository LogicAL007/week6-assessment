#Write a function that accepts the age of 4 people and displays the oldest
def find_oldest(age):
    oldest = max(age)
    print("The oldest age is " + str(oldest))
age = [int(input("Enter age of person {}: ".format(i + 1))) for i in range(4)]
find_oldest(age)
