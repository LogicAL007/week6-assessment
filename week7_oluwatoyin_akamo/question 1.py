def check_range(number, lowest_number, highest_number):
  return lowest_number <= number <= highest_number

print(check_range(0, 10, 100))
print(check_range(2, 1, 100))
print(check_range(3, 10, 100))