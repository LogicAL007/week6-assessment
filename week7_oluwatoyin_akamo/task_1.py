""" A function that check if a number is in a given range"""
def num_check(num, begin, end):
    if begin <= num <= end:
        return True
    else:
        return False
    
# this is a test of the program.
# user input is included for flexibility if the code
user_input = int(input("give a number: "))
user_brange= int(input("give the beginnning range: "))
user_erange= int(input("give the end range: "))

view = num_check(user_input, user_brange, user_erange)
print(view)
