# Definition of my function and setting a random range, specifying the start of the range, and its end
def check_if_number_falls_in_range (start, end):

    # Here, i specified the variable "entered number", and created a prompt that will ask the user to enter a random number. 
    # Next, I used the 'int' function to convert the entered string, to an integer.
    entered_number = int(input("please enter a random number, sit back, while we check its position for you:"))

    # Here i defined the range arguments "start" as 25 and "end" as 50
    start = 25
    end = 100

   # Here, I used conditional operators to setup the conditions for the "if" and "else" statements
    if entered_number >= start and entered_number <= end:
        print(f"{entered_number} falls in the specified range of integers .")
    else:
        print("OOPPSSS !!!!! Please try again")

# Lastly, i called the function, to check if the entered number falls within the specified range, having set all conditions.
check_if_number_falls_in_range(25, 100)
