# Here, I defined the fucnction using the "def" function
def find_the_youngest_person_amongst_four_randomly_entered_ages() :
    
    # Here, i initialized and created a storage for list
    randomly_selected_ages = []

    # Here, i used a loop that would occur 4 times, asking the user to enter ages up to 4 different times
    for i in range(4):
        randomly_selected_age = int(input(f"Kindly Enter The Age of Person {i+1}: "))

        # Here, I obtained the 4 different ages, and added (appended) them the earlier created empty list storage
        randomly_selected_ages.append(randomly_selected_age)

    # Here, i obtained the youngest person, using the 'min' function
    youngest_person = min(randomly_selected_ages)

    # Here, I used the f-string to fetch out the age of the youngest person, as specified earlier.
    print(f"The person with the youngest age is {youngest_person} years old on planet earth")

# Lastly, i called out the function.
find_the_youngest_person_amongst_four_randomly_entered_ages()