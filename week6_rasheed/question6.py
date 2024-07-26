def find_youngest(age1, age2, age3, age4):
    # Create a list of the ages
    ages = [age1, age2, age3, age4]
    
    # Find the maximum age
    youngest_age = min(ages)
    
    # Print the oldest age
    print(f"The youngest age is: {youngest_age}")
find_youngest(22, 25, 31, 20)