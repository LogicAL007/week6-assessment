# Write a Python function that accepts a string and counts the number
# of upper and lower letters( hint: use built-in function isupper() and
# islower()).

def count_upper_lower(string):
    lowercase_letter_count = 0
    uppercase_letter_count = 0

    for letter in string:
        if letter.isupper():
            uppercase_letter_count += 1
        elif letter.islower():
            lowercase_letter_count += 1
    print(f"Upper case letters: {uppercase_letter_count}")
    print(f"Lower case letters: {lowercase_letter_count}")


count_upper_lower("You Are Welcome")

