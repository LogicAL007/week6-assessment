def count(words):
    capital = 0
    small = 0
    for word in words:
        if word.isupper():
            capital += 1
        elif word.islower():
            small += 1
    return [capital, small]

user_input = input("give the words to count: ")

result = count(user_input)
print("This is the analysis:")
print("\t-uppercase word(s) is/are "+ str(result[0]))
print("\t-lowercase word(s) is/are "+ str(result[1]))
