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
