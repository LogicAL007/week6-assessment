# Here, I defined the fucnction using the "def" function
def obtain_the_total_of_the_first_ten_even_numbers_starting_from_2() :

    # Here, i assigned a variable to add a range of values from 2 to 21, with a step of 2, counting 10 numbers, which automatically be even.
    overall_sum_of_the_digits = sum(range(2, 21, 2))

    # Here, i used the f-string function to include the Summed value of the earlier assigned variable.
    print(f"The total obtained from the first ten even numbers gives {overall_sum_of_the_digits}")

# Lastly, i called out the function.
obtain_the_total_of_the_first_ten_even_numbers_starting_from_2()
