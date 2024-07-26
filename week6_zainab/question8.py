number = int(input("even num"))
count = 0
even_number = 0
for num in range(number):
    if num%2 ==0 and count<=10:
        count = count+1
        even_number = even_number + num
print(even_number)
