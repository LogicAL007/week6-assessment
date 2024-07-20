#task 3
number = int(input("enter a positive integer here: "))
for i in range(1, number+1):
    if number % i == 0:
        print(i)
