# Ask the user for a positive integer
number = int(input("Please enter a positive integer: "))

# Check if the number is positive
if number <= 0:
    print("Please enter a positive integer.")
else:
    # Find and print all divisors of the number
    print(f"The divisors of {number} are:")
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)