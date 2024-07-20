#task 8
count = 0
num = 0
sum = 0

while count < 10:
    if num % 2 == 0:
        print(num)
        sum += num
        count += 1
    num +=1
print(f"The sum of the first 10 even numbers is: {sum}")