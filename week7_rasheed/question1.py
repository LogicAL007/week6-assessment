def random_number(number, start, end):
    return start <= number <= end

number = 83
start = 1
end = 100

if random_number(number, start, end):
    print(f"The number {number} falls within the range {start} to {end}.")
else:
    print(f"The number {number} does not fall within the range {start} to {end}.")