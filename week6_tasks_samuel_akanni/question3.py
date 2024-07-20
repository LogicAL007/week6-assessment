#Write a program that asks for a positive integer and prints all of its divisors,
#one by one, on separate lines in ascending order. 
#A divisoris a number that divides a particular number with no remainder. 
#For example, the divisors of 4 are 1, 2, and 4. To check if a is a divisor of b, you can use the modulo operator %. 
#a % b returns the remainder of dividing a by b. For example, 9 % 2 is 1 because 9 = (4 * 2) + 1,
#and 9 % 3 is 0 because 9 divides into 3 with no remainder. If a % b == 0, then b is a divisor of a.

number = int(input("Enter a positive integer (e.g 4, 50, 22): "))
print("Divisors of the number are:")
for i in range(1, number + 1):
    if number % i == 0:
        print(i)