#Write a function that accepts the age of 4 people and displays the oldest
def find_oldest(age):
    oldest = max(age)
    print(f"The oldest age is {oldest}")
age = [int(input(f"Enter age of person {i+1}: ")) 
        for i in range(4)]
find_oldest(age) 