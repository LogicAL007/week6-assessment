# Here, I defined the fucnction using the "def" function.
def check_if_the_entered_year_is_a_leap_year_or_not():

    # Here assigned a variable, and specified a prompt that allows the users to enter an integer.
    selected_year = int(input("Please enter any year of your choice: "))

    # Here, i used the "if conditional statement" to check the conditions that should be met,
    # I also used the 'and' and 'or' statements to join the two conditions that are being checked.
    # then prints the interpolated string is the two differerent conditions are met or otherwise.
    if (selected_year % 4 == 0 and selected_year % 100 != 0) or (selected_year % 400 == 0):
        print(f"{selected_year} is indeed a leap year")

    else:
        print(f"{selected_year} is not a leap year")

# Lastly, i called the function.
check_if_the_entered_year_is_a_leap_year_or_not()
