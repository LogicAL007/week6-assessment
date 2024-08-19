Number = int(input('Give me a positive integer: '))
divisor = []

for num in range(1, Number + 1):
    if Number % num == 0:
        divisor.append(num)
    else:
        continue

print("This is the divisor of the number you've choosen:")
for factor in divisor:
    print(factor)