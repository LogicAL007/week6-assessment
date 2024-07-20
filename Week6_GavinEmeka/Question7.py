# Here, I defined the fucnction using the "def" function
def obtain_the_total_of_the_first_ten_natural_numbers() :

    # Here, i assigned a variable to add a range of values from 1 to 10, with no step
    overall_sum_of_the_digits = sum(range(1, 11))

    # Here, i used the f-string function to include the Summed value of the earlier assigned variable.
    print(f"The total obtained from the first ten natural numbers gives {overall_sum_of_the_digits}")

# Lastly, i called out the function.
obtain_the_total_of_the_first_ten_natural_numbers()


