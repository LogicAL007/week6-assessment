 # Here, I defined the fucnction using the "def" function.
def count_the_number_of_Upper_and_lower_Case_Letters():
    
    # Here I assigned a variable, and specified a prompt that allows the users to enter any string of their chooice.
    entered_text = input("enter your choice sentence, relax while we count the letter-case distribution in your entry: ")

    # Here i reset my counts, to start counting from Zero
    uppercase_letters_count = 0
    lowercase_letters_count = 0

    # Here,i brought in the use of the for loop, to check through the characters that would be entered by the users, and also incorperating the if and elif conditions
    
    for char in entered_text:
        if char.isupper():
            uppercase_letters_count += 1
        elif char.islower():
            lowercase_letters_count += 1

# Here,I Printed out my results     
    print(f"The number of Uppercase letters in your text is: {uppercase_letters_count}")
    print(f"The number of Lowercase Letters in your text is: {lowercase_letters_count}")

# Here, I called the function
count_the_number_of_Upper_and_lower_Case_Letters()



# More practices
def the_case_distribution_of_letters_in_a_given_text():
    enter_text =input("enter the text you wanna count: ")
    capital_letters = 0
    small_letters = 0
    for char in enter_text:
        if char.isupper():
            capital_letters += 1
        elif char.islower():
            small_letters += 1
    print(f"You have {capital_letters} Uppercase letters in the text you entered")
    print(f"You have {small_letters} Lowercase letters in the text you entered")
the_case_distribution_of_letters_in_a_given_text()




# More Practices
def check_number_in_range(start, end):
    number = int(input("enter your number: "))
    start = 20
    end = 93
    if number >= start and number <= end:
        print(f"{number} is in the range")
    else:
        print(f"{number}is not in the range")
check_number_in_range(20, 93)




def concatenate(a="Data Epic", b="has", c="cool", d="Mentors", e="!"):
    print (a + " " + b + " " + c + " " + d + " " + e)

concatenate(a="Data Epic", b="has", c="cool", d="Mentors", e="!")