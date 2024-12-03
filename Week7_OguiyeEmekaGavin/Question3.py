# Here, i Defined the function using the "def" keyword
def return_distinct_list():
    
    # Next, I Initialized an empty list to store the enteries of the favorite colors
    favorite_colors = []

    # Here, I Looped within the range of 10, to ask the users for their favorite colors
    for i in range(10):
        color = input(f"Hey user {i+1}, what is your favorite color?  : ")
        # Next, I Added the Users favorite colors to the list
        favorite_colors.append(color)

    # Return the set of distinct favorite colors
    return list(set(favorite_colors))

# Call the function
distinct_colors = return_distinct_list()
print(distinct_colors)