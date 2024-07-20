# Here, I defined the fucnction using the "def" function.
def print_all_divisors_on_separate_lines():

    # Here, I assigned the variable, POSITIVE INTEGER, and specified that its in the "int" type
    positive_integer = int(input("Enter a positive integer: "))

    # Here, I emplyed the use of Logical operators to set conditions for the positive integer
    if positive_integer > 0:
        print(f"Divisors of {positive_integer}:")

    # Here, I used the loop variable, 'i' to range the positive integer, as arranged to move on to the next line, in ascending order.
    for i in range(1, positive_integer + 1):
        # Here, i set a modulo condition, to check if the divident has a remainder that is exactly '0', 
        # and prints the value, is condition is satisfied.
        if positive_integer % i == 0:
            print(i)

# Here, lastly i called the function
print_all_divisors_on_separate_lines()

